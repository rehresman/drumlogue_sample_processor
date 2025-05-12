# MacOS Sample Processor for the KORG drumlogue

This automates the annoying parts of uploading samples to the KORG drumlogue on **MacOS**.

The pain points I've encountered are:

1. MacOS adds hidden files when doing certain file operations. But since we only have 32mb of space to work with, we really need to delete those files before copying them over to the drumlogue.

2. Manually keeping track of sample numbers is difficult and slow.  My samples were organized before the drumlogue, why do it again?  And if I add a new cymbal sample, I don't want it to be at slot 115, I want it with the other cymbals.

### So here's what this code does:

**1. organize_samples.py**
This organizes and formats sample file names within a folder in the way the drumlogue wants to receive them. It orders them alphabetically, and you can tell it to add certain samples to the beginning of the list (how-to at the end of this document).

**2. copy_to_drumlogue.py**
This deletes all samples and hidden garbage off your drumlogue and copies over samples from whatever folder you give it.  It only affects the Samples folder in the drumlogue.

So now you can easily organize and transfer your files.

## Installation

Just download the code and unzip the files.  Running python code on your Mac may seem intimidating the first time, but it's incredibly easy if you use something like ChatGPT to help you.  If you get error messages, just copy and paste them into ChatGPT and it will translate the computer language to something more understandable, and tell you how to fix it.


## Usage

Before you do anything, **make a backup of your samples**.  This code deletes all files in a directory except the .wav files, so if you make a mistake it *will* delete things.  Similarly, if there's an error during data transfer, **files will be lost, so make a backup**. 


## 1.
Plug in the drumlogue to your computer via USB.  While holding down the *'record'* button, power it on. 
## 2. 

Get the pathname to the *CODE* folder you just unzipped.  This will look something like this: 
```bash
/Users/ryan/Downloads/korg_drumlogue_sample_processor/
```

But of course it won't say "ryan." Make sure it has a backslash at the end of it like mine does.  Copy and paste it to a notepad document for later use.  

## 3.

Next you need to get the pathname to your *SAMPLES* folder.  This should be a folder containing **ONLY** the samples you want to send to the drumlogue.  Everything else in the folder will be deleted. It will look something like the following:
```
/Users/ryan/Documents/samples/
```

Copy and paste this one to your notepad too.  Make sure it has a backslash.

## 4.

Next, in Terminal run the following, inserting the *CODE* and *SAMPLES* pathnames from steps 2 and 3.

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
Now your samples folder should be properly formatted.  Check Terminal for any errors.

## 5.

Next, we will delete all current samples and junk files off the drumlogue, and copy over our new clean ones.

```bash
python (INSERT CODE PATHNAME HERE!!!)/copy_to_drumlogue.py (INSERT SAMPLES PATHNAME HERE!!!)
```

**Example**

```bash
 python3 /Users/ryan/Downloads/korg_drumlogue_sample_processor/copy_to_drumlogue.py /Volumes/T7/Everything/samples
```

## 6.
You survived!  Press *play* on the drumlogue and have fun!  In summary, we just ran two python files on your samples folder.

## Final Notes
This code is slightly customizable too.  If you open organize_samples.py with any text editor (like your notes app), you'll see something up at the top called *SPECIAL_ORDER*.  Any filenames you put in that list will be the first user samples on your drumlogue.  Mine are sub.wav and sub_kick.wav, but if you put your own in there it will work!  Be sure to format them like I did:
```python
SPECIAL_ORDER = ['something.wav', 'something_else.wav']
```