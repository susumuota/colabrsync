# colabrsync

Run rsync periodically on background on Google Colab.

## Usage

```python
!pip install colabrsync

from google.colab import drive
drive.mount('/content/drive')

!mkdir -p /content/outputs
!mkdir -p /content/drive/MyDrive/outputs

from colabrsync import RsyncMirror

rsm = RsyncMirror('/content/outputs/', '/content/drive/MyDrive/outputs/')

!diff -ur /content/outputs /content/drive/MyDrive/outputs

!touch /content/outputs/newfile.txt

!diff -ur /content/outputs /content/drive/MyDrive/outputs

!sleep 60

!diff -ur /content/outputs /content/drive/MyDrive/outputs

del rsm

!ls -l /content/outputs /content/drive/MyDrive/outputs
```

## License

MIT License, See LICENSE file.

## Author

Susumu OTA
