<p align="center">
  <img src="https://github.com/MrPenguin07/dolphin.shred-it/assets/127086564/5038c302-28d6-4ece-8986-ca87577af14a" alt="dolphin shred-it-128x128" />
</p>

<h1 align="center">
  Dolphin Shred-it
</h1>


**Dolphin right click context menu -> Shred files/dir**  
Securely delete your files from within the Dolphin file manager!

```
 .
├──  gtk-version
│  ├──  shred-it.desktop
│  ├──  shred-it.png
│  └──  shred-it.py
├──  usr
│  └──  share
│     └──  kio
│        └──  servicemenus
│           ├──  shred-it.desktop
│           ├──  shred-it.png
│           └──  shred-it.py
├──  LICENSE
├──  README.md
└──  requirements.txt
```

Dependencies: 
- Dolphin
- `PyQt5`  
  `notify2`
- `shred` - part of the [Coreutils](https://www.gnu.org/software/coreutils/) package, incl. in most distros base installation.

## INSTALL
**System Wide**
```
$ git clone https://github.com/MrPenguin07/dolphin.shred-it.git && cd dolphin.shred-it
$ sudo cp usr/share/kio/servicemenus/* /usr/share/kio/servicemenus/
$ sudo chmod +x /usr/share/kio/servicemenus/shred.py
```
**Local User**
```
$ git clone https://github.com/MrPenguin07/dolphin.shred-it.git && cd dolphin.shred-it
$ cp usr/share/kio/servicemenus/* ~/.local/share/kio/servicemenus
$ chmod +x ~/.local/share/kio/servicemenus/shred.py
```
_There is an optional GTK3 version of the script, use this version with instructions as above_

#### Add the context menu in dolphin settings;

![image](https://github.com/MrPenguin07/dolphin-shredder/assets/127086564/505c97c7-68d0-4bd8-8b23-ea14f575a244)

#### Right-click context menu;

![image](https://github.com/MrPenguin07/dolphin-shredder/assets/127086564/7736015e-c175-456a-9a78-7229b60e6895)

#### Qt5 Confirmation;

![image](https://github.com/MrPenguin07/dolphin-shredder/assets/127086564/2ead02c7-2510-486e-8fe5-5e86f99d13ff)



## Notes

**The default is 5 passes, can be changed within shred.py**  
`SHRED_ITERATIONS = 5`

May also be run from the shell;  
`$ python3 shred.py <file/dir>`

## Caveats/Limitations

When using `shred` for secure file deletion, it's important to be aware of the following limitations:

- **Snapshot File Systems**: Ineffective on file systems configured to use snapshots as snapshots may retain copies of the data.
  
- **Journaling File Systems**:
  + _Somewhat effective_ on file systems that focus on metadata journaling (e.g. ext4 with the default `data=ordered`).
  + Less effective on file systems that journal both metadata and file data.

- **SSD and Wear Leveling**: Varied effectiveness on SSDs due to firmware & wear leveling algorithms.
  
- **RAID Systems**: On RAID configurations with parity, old data may remain recoverable even after `shred` has been run.

These caveats are also faced by bleachbit and other more professional tools, they are inherent to modern disks & filesystems.  
This app is NOT designed for professional grade data destruction, however it should prove effective for;
  - Personal info, Bank statements, Work files you took home and finished using etc.
    
**For more reliable secure deletion options, consider low level tools.**

