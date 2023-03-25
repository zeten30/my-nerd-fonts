#!/bin/bash

mkdir -p sources

# Clean old sources
rm -rf sources/*
cd sources || exit 1

for FNT in Hack SourceCodePro CascadiaCode Overpass FiraCode RobotoMono JetBrainsMono; do
  wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/${FNT}.zip
  unzip ${FNT}.zip
done

mkdir -p my-nerd-fonts
mv ./*.ttf ./*.otf my-nerd-fonts/
tar cfz my-nerd-fonts.tgz my-nerd-fonts
rm -rf ./*.zip ./my-nerd-fonts

# Create source tarball
mkdir -p ../rpmbuild/
rm -rf ../rpmbuild/*.*

# Back to buildroot
cd ../ || exit 1
