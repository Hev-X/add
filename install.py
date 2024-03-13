import subprocess

backup = {
        'hubert_base.pt':'https://drive.google.com/file/d/1tHNmjoSHJj7G2xX_Knz4zZ8Mg7g-VhAW/view?usp=sharing',
        'pretrained_v2/D40k.pth':'https://drive.google.com/file/d/1BJ3TKdn2xAK9VbV8UIDoo_9K4Yyfjs7-/view?usp=sharing -O pretrained_v2/D40k.pth',
        'pretrained_v2/G40k.pth':'https://drive.google.com/file/d/1BJ3TKdn2xAK9VbV8UIDoo_9K4Yyfjs7-/view?usp=sharing -O pretrained_v2/G40k.pth',
        'pretrained_v2/f0D40k.pth':'https://drive.google.com/file/d/1A33v5MT1L_-v4iP550ibl5givEqgDus1/view?usp=sharing -O pretrained_v2/f0D40k.pth',
        'pretrained_v2/f0G40k.pth':'https://drive.google.com/file/d/1mMEOosc4FO3QRhYxIhHr-GVCxF05tjwV/view?usp=sharing -O pretrained_v2/f0G40k.pth',
        'rmvpe.pt':'https://drive.google.com/file/d/1ABwfoHKBlUsyGIy-f_axaHM6vcXxZzQU/view?usp=drive_link'
}

def aria_backup(missing_file):
    url = backup[missing_file]
    subprocess.run(['gdown', '--fuzzy', url])



if not "installed" in locals():
    subprocess.run(['wget', 'https://github.com/777gt/EVC/raw/main/wav2lip-HD.tar.gz'])
    subprocess.run(['wget', 'https://github.com/777gt/EVC/raw/main/wav2lip-cache.tar.gz'])
    subprocess.run(['tar', '-zxvf', '/content/wav2lip-cache.tar.gz', '-C', '/'])
    subprocess.run(['tar', '-xvf', '/content/wav2lip-HD.tar.gz', '-C', '/content'])
    if gdrive:
        subprocess.run(['wget', 'https://github.com/777gt/EVC/raw/main/Packages.tar.gz', '-O', '/content/drive/MyDrive/RVC_Packages/Packages.tar.gz'])
        subprocess.run(['tar', '-zxvf', '/content/drive/MyDrive/RVC_Packages/Packages.tar.gz', '-C', '/'])
    else:
        subprocess.run(['wget', 'https://github.com/777gt/EVC/raw/main/Packages.tar.gz', '-O', '/content/Packages.tar.gz'])
        subprocess.run(['tar', '-zxvf', '/content/Packages.tar.gz', '-C', '/'])
    subprocess.run(['pip', 'install', '-q', 'gTTS', 'torchcrepe'])
    subprocess.run(['pip', 'install', 'gradio', '--upgrade'])
    subprocess.run(['git', 'clone', 'https://github.com/777gt/-EVC-'])
    subprocess.run(['wget', 'https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.pt'])
    subprocess.run(['wget', 'https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt'])
    subprocess.run(['wget', 'https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D40k.pth', '-O', '/content/-EVC-/pretrained_v2/D40k.pth'])
    subprocess.run(['wget', 'https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G40k.pth', '-O', '/content/-EVC-/pretrained_v2/G40k.pth'])
    subprocess.run(['wget', 'https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D40k.pth', '-O', '/content/-EVC-/pretrained_v2/f0D40k.pth'])
    subprocess.run(['wget', 'https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G40k.pth', '-O', '/content/-EVC-/pretrained_v2/f0G40k.pth'])
    for file in list(backup.keys()):
        if not os.path.exists(file):
            aria_backup(file)
    installed=True

if gdrive:
    if os.path.exists('/content/drive/MyDrive/RVC'):
        subprocess.run(['mkdir', '-p', '/content/drive/MyDrive/RVC'])
        subprocess.run(['cd', '/content/drive/MyDrive/RVC'])
    else:
        subprocess.run(['mkdir', '-p', '/content/drive/MyDrive/RVC'])
        subprocess.run(['cd', '/content/drive/MyDrive/RVC'])
        subprocess.run(['wget', 'https://github.com/777gt/EVC/raw/main/Packages.tar.gz', '-O', '/content/Packages.tar.gz'])
        subprocess.run(['tar', '-zxvf', '/content/Packages.tar.gz', '-C', '/'])
    subprocess.run(['mkdir', '-p', '/content/unzips'])
    for file in os.listdir():
        if file.endswith('.zip'):
            file_name=file.split('.')[0]
            zip_path = f'/content/drive/MyDrive/RVC/{file}'
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                for member in zip_ref.infolist():
                    if member.filename.endswith('.pth'):
                        extraction_dir=f'/content/unzips/{file_name}'
                        file_size = member.file_size
                        if file_size < 100 * 1024 * 1024:
                            with zip_ref.open(member) as file:
                                if len(file.read()) < 100 * 1024 * 1024:
                                    zip_ref.extract(member, path=extraction_dir)
                                    subprocess.run(['find', '/content/unzips/{file_name}', '-name', '*.pth', '-exec', 'mv', '{}', '/content/-EVC-/weights/{file_name}.pth', ';'])
                    if member.filename.endswith('.index'):
                        extraction_dir=f'/content/unzips/'
                        with zip_ref.open(member) as file:
                            zip_ref.extract(member, path=extraction_dir)
                            subprocess.run(['mkdir', '-p', '/content/-EVC-/logs/{file_name}'])
                            os.chdir(f"/content/-EVC-/logs/{file_name}")
                            subprocess.run(['find', '/content/unzips', '-name', '*.index', '-exec', 'mv', '{}', '.', ';'])

if os.path.exists('/content/unzips'):
    shutil.rmtree('/content/unzips')

if tensorboard:
    subprocess.run(['pip', 'install', 'tensorboard'])
    subprocess.run(['tensorboard', '--logdir', '/content/-EVC-/logs'])

subprocess.run(['mkdir', '-p',
