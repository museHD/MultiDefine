# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['vocab_list.py'],
             pathex=['D:\\PROGRAMMING\\PYTHON SCIRPTS\\Scrapers'],
             binaries=[('D:\\PROGRAMMING\\PYTHON SCIRPTS\\Scrapers\\chromedriver.exe', '.')],
             datas=[('C:\\Program Files (x86)\\Python37-32\\Lib\\site-packages\\pyfiglet', './pyfiglet')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='vocab_list',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
