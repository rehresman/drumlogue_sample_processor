import os
import sys

MAX_FILES = 128
MAX_SIZE_MB = 32
SPECIAL_ORDER = ['sub.wav', 'sub_kick.wav']

def is_wav_file(file):
    return file.lower().endswith('.wav')

def get_clean_name(filename):
    return filename.split('_', 1)[-1] if '_' in filename else filename

def get_total_folder_size(folder):
    return sum(
        os.path.getsize(os.path.join(folder, f))
        for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    )

def main():
    numWavFiles = 0
    if len(sys.argv) != 2:
        print("Usage: python3 organize_samples.py /path/to/folder")
        sys.exit(1)

    folder = sys.argv[1]

    if not os.path.isdir(folder):
        print(f"❌ Error: '{folder}' is not a valid directory.")
        sys.exit(1)

    # Step 0: Sanity check: make sure there's at least one .wav file
    for f in os.listdir(folder):
        if is_wav_file(f):
            numWavFiles += 1
    if numWavFiles == 0:
        print("❌ Error: No .wav files found in the target directory! Please check the samples pathname.")
        sys.exit(1)

    # Step 1: Remove non-wav and hidden files
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if not is_wav_file(f) or f.startswith('.'):
            print(f"Removing: {f}")
            os.remove(path)

    # Re-list files after deletion
    files = [f for f in os.listdir(folder) if is_wav_file(f)]

    # Step 2: Check file count
    if len(files) > MAX_FILES:
        print(f"❌ Error: {len(files)} .wav files found. Limit is {MAX_FILES}.")
        sys.exit(1)

    # Step 3: Check total size
    file_sizes = [(f, os.path.getsize(os.path.join(folder, f))) for f in files]
    total_size = sum(size for _, size in file_sizes)
    if total_size > MAX_SIZE_MB * 1024 * 1024:
        top_files = sorted(file_sizes, key=lambda x: x[1], reverse=True)[:5]
        print(f"❌ Error: Total size is {total_size / (1024 * 1024):.2f} MB. The official limit is {MAX_SIZE_MB} MB, but in practice, it may be more like {MAX_SIZE_MB - 1}.")
        print("Top 5 largest files:")
        for fname, size in top_files:
            print(f"  {fname}: {size / 1024:.2f} KB")
        sys.exit(1)

    # Step 4: Strip prefixes
    stripped_names = {}
    for f in files:
        stripped = get_clean_name(f)
        stripped_names[f] = stripped

    # Step 5: Rename with new prefixes
    renamed_files = []

    def rename_file(old, new_prefix):
        new_name = f"{new_prefix:03d}_{stripped_names[old]}"
        os.rename(os.path.join(folder, old), os.path.join(folder, new_name))
        renamed_files.append(new_name)

    # Handle special files
    prefix = 1
    for name in SPECIAL_ORDER:
        match = [f for f in files if stripped_names[f] == name]
        if match:
            rename_file(match[0], prefix)
            files.remove(match[0])
            prefix += 1

    # Remaining files sorted alphabetically
    remaining = sorted([f for f in files if f not in renamed_files], key=lambda f: stripped_names[f])
    for f in remaining:
        if prefix > 128:
            print("❌ Error: Ran out of prefix numbers.")
            sys.exit(1)
        rename_file(f, prefix)
        prefix += 1

    final_size_mb = get_total_folder_size(folder) / (1024 * 1024)
    print(f"✅ Done organizing samples. Total folder size: {final_size_mb:.2f} MB")

if __name__ == "__main__":
    main()
