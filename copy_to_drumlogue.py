import os
import sys
import shutil

DEST_FOLDER = '/Volumes/drumlogue/Samples'
VOLUME_ROOT = '/Volumes/drumlogue'

def is_wav_file(file):
    return file.lower().endswith('.wav')

def get_free_space_bytes(path):
    """Return free space in bytes on the given filesystem path."""
    stat = os.statvfs(path)
    return stat.f_bavail * stat.f_frsize

def get_total_size_bytes(folder):
    """Return total size in bytes of all .wav files in the folder."""
    total = 0
    for f in os.listdir(folder):
        if is_wav_file(f):
            full_path = os.path.join(folder, f)
            if os.path.isfile(full_path):
                total += os.path.getsize(full_path)
    return total

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 copy_to_drumlogue.py /path/to/source/folder")
        sys.exit(1)

    source_folder = sys.argv[1]

    if not os.path.isdir(source_folder):
        print(f"❌ Error: '{source_folder}' is not a valid directory.")
        sys.exit(1)

    if not os.path.exists(DEST_FOLDER):
        print(f"❌ Error: Destination folder '{DEST_FOLDER}' not found. Is the drumlogue mounted?")
        sys.exit(1)

    # Step 1: Delete everything in DEST_FOLDER
    print(f"🧹 Clearing out {DEST_FOLDER}...")
    for f in os.listdir(DEST_FOLDER):
        full_path = os.path.join(DEST_FOLDER, f)
        try:
            if os.path.isfile(full_path) or os.path.islink(full_path):
                os.remove(full_path)
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)
            print(f"Deleted: {f}")
        except Exception as e:
            print(f"⚠️ Couldn't delete {f}: {e}")

    # Step 2: Check space before copying
    free_bytes = get_free_space_bytes(VOLUME_ROOT)
    files_to_copy_size = get_total_size_bytes(source_folder)

    print(f"📦 Files to copy: {files_to_copy_size / (1024 * 1024):.2f} MB")
    print(f"💾 Free space on drumlogue: {free_bytes / (1024 * 1024):.2f} MB")

    if files_to_copy_size >= free_bytes:
        print("❌ Error: Not enough space on drumlogue to copy files.")
        sys.exit(1)

    # Step 3: Copy files
    print(f"📤 Copying files to {DEST_FOLDER}...")
    copied_count = 0
    for f in os.listdir(source_folder):
        if is_wav_file(f):
            src_path = os.path.join(source_folder, f)
            dst_path = os.path.join(DEST_FOLDER, f)
            shutil.copy2(src_path, dst_path)
            copied_count += 1
            print(f"Copied: {f}")

    print(f"✅ Done. {copied_count} .wav files copied to drumlogue. Press 'play' to initialize new samples on your drumlogue.")

if __name__ == "__main__":
    main()
