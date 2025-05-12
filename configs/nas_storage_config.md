# Synology NAS Storage Configuration

- **Device Name:** DeathStar
- **Admin Username:** kevin
- **Storage Pool RAID Type:** SHR (Synology Hybrid RAID)
- **Drive Type:** SATA HDD
- **Drives:**
  - Drive 1: 12TB
  - Drive 2: 12TB
- **Estimated/Allowed Capacity:** 11,165 GB
- **File System:** BTRFS
- **Encryption:** Not enabled 

---

## Folder Structure & Permissions (as of May 11)

### /volume1/configs
```
drwxrwxrwx+ 1 root       root     8 May 11 12:45 @eaDir
drwxrwxrwx+ 1 dockeruser docker  46 May 11 13:05 plex
drwxrwxrwx+ 1 dockeruser docker 254 May 11 15:37 prowlarr
drwxrwxrwx+ 1 dockeruser docker  80 May 11 13:25 qbittorrent
drwxrwxrwx+ 1 dockeruser docker 186 May 11 16:47 radarr
drwxrwxrwx+ 1 kevin      users    0 May 11 17:00 sonarr
drwxrwxrwx+ 1 kevin      users    0 May 11 17:50 recyclarr
```

### /volume1/data
```
drwxrwxrwx+ 1 root  root  8 May 11 12:38 @eaDir
drwxrwxrwx+ 1 kevin users 0 May 11 13:41 movies
drwxrwxrwx+ 1 kevin users 0 May 11 17:01 tv
```

---

## Downloads Folder Structure (as of May 11)

### /volume1/downloads
```
drwxrwxrwx+ 1 root  root    8 May 11 12:45 @eaDir
drwxrwxrwx+ 1 kevin users 502 May 11 17:37 torrents
```

### /volume1/downloads/torrents
```
drwxrwxrwx+ 1 kevin      users     0 May 11 17:22 completed
drwxrwxrwx+ 1 kevin      users     0 May 11 17:22 incomplete
``` 