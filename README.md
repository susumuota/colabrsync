# colabrsync

Run rsync periodically on background on Google Colab.

## Usage

```python
!pip install colabrsync

from google.colab import drive
drive.mount('/content/drive')

from colabrsync import RsyncMirror

!mkdir -p /content/outputs
!mkdir -p /content/drive/MyDrive/outputs

rsm = RsyncMirror('/content/outputs', '/content/drive/MyDrive/outputs')

!touch /content/outputs/newfile.txt

!sleep 60
!ls -l /content/drive/MyDrive/outputs

del rsm

!diff -ur /content/outputs /content/drive/MyDrive/outputs
```

## License

MIT License, See LICENSE file.

## Author

Susumu OTA
