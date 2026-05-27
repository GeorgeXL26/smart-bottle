# Pico 2 Code Deployment Guide

## Prerequisites

```bash
mpremote connect /dev/cu.usbmodem1101
```
> If `mpremote` is not found, run:
> ```bash
> export PATH="$HOME/Library/Python/3.9/bin:$PATH"
> ```

---

## 1. Remote Test (Pico connected to Mac via USB)

Run a script once to test it:

```bash
mpremote run python-code/test_led.py
```

Open a live REPL (interactive shell):

```bash
mpremote
```

Exit the REPL with `Ctrl+A` then `Ctrl+X`.

---

## 2. Copy Code to Pico (standalone mode)

To make the Pico run code automatically when powered on, save it as **`main.py`** on the Pico's internal storage.

### Upload a file

```bash
mpremote cp local_file.py :main.py
```

### Upload a whole folder

```bash
mpremote cp -r python-code/ :
```

### List files on the Pico

```bash
mpremote ls
```

### Delete a file from the Pico

```bash
mpremote rm main.py
```

---

## 3. Run Standalone (no computer)

1. Upload your code as `main.py` (see section 2)
2. Unplug the Pico from USB
3. Power it via battery pack or USB power bank
4. The Pico runs `main.py` automatically on boot

To see what's running, reconnect to USB and open the REPL (`mpremote`).

---

## Common Workflow

```
Write code → mpremote run test.py → Debug → Upload as main.py → Run standalone
```
