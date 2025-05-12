# MacOS Sample Processor for the KORG drumlogue

This automates the annoying parts of uploading samples to the KORG drumlogue on **MacOS**.

The pain points I've encountered are:

1. MacOS adds hidden files when doing certain file operations. But since we only have 32mb of space to work with, we really need to delete those files before copying them over to the drumlogue.  

2. Organizing files is difficult.  Maybe I want to move all my 32 cymbal samples to slots 001-032.  This program orders samples alphabetically and adds all required prefixes...so if you were organized before the drumlogue, you don't have to do it again. 

So I made these little python scripts to handle them.

## Installation

Just download the code and unzip the files.  Running python code on your Mac may seem intimidating the first time, but it's incredibly easy if you use something like ChatGPT to help you.  If you get error messages, just copy and paste them into ChatGPT and it will translate the computer language to something more understandable, and tell you how to fix it.


## Usage

Before you do anything, **make a backup of your samples**.  This code deletes all files in a directory except the .wav files, so if you make a mistake it *will* delete things.  Similarly, if there's an error during the copying process (like if you run out of memory on the drumlogue), **files will be lost, so make a backup**. 


## 1.
Plug in the drumlogue to your computer via USB.  While holding down the *'record'* button, power it on. 
## 2. 

Next you need to get the pathname to the *CODE* folder you just unzipped.  This will look something like this: 
```bash
/Users/ryan/Downloads/korg_drumlogue_sample_processor/
```

But of course it won't say "ryan." Make sure it has a backslash at the end of it like mine does.  Ask ChatGPT for help if you get stuck.  Copy and paste it to a notepad document for later use.  

## 3.

Next you need to get the pathname to your *SAMPLES* folder.  This should be a folder containing **ONLY** the samples you want to send to the drumlogue.  Everything else will be deleted. It will look something like the following:
```
/Users/ryan/Documents/samples/
```

Copy and paste this one to your notepad too.  Make sure it has a backslash.

## 4.

Next, in Terminal run the following, inserting the *CODE* and *SAMPLES* pathnames.

```bash
python (INSERT CODE PATHNAME HERE!!!)/organize_samples.py (INSERT SAMPLES PATHNAME HERE!!!)
```

Or if that doesn't work:

```bash
python3 (INSERT CODE PATHNAME HERE!!!)/organize_samples.py (INSERT SAMPLES PATHNAME HERE!!!)
```

Some Macs like it if you use the python3 command instead.

**Example**

```bash
 python3 /Users/ryan/Downloads/korg_drumlogue_sample_processor/organize_samples.py /Volumes/T7/Everything/samples
```

## 5.

Now your samples folder should be properly formatted.  Check Terminal for any errors.  Next, we will delete all current samples and junk files off the drumlogue, and copy over our new clean ones.

```bash
python (INSERT CODE PATHNAME HERE!!!)/copy_to_drumlogue.py (INSERT SAMPLES PATHNAME HERE!!!)
```

**Example**

```bash
 python3 /Users/ryan/Downloads/korg_drumlogue_sample_processor/copy_to_drumlogue.py /Volumes/T7/Everything/samples
```

## 6.
You survived!  Press *play* on the drumlogue and have fun!

## Final Notes
This code is slightly customizable too.  If you open organize_samples.py with any text editor (like your notes app), you'll see something up at the top called *SPECIAL_ORDER*.  Any filenames you put in that list will be the first user samples on your drumlogue.  Mine are sub.wav and sub_kick.wav, but if you put your own in there it will work!