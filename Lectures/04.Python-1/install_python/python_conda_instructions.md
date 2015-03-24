# Python Conda Installation Instructions (MAC/Linux)


1. Download the installer for [Python 3.4 for Mac](http://repo.continuum.io/miniconda/Miniconda3-3.8.3-MacOSX-x86_64.sh)
2. To install miniconda on a mac, run: `sh Miniconda3-3.8.3-MacOSX-x86_64.sh`
3. If you're using Linux, this is your installer for [Python 3.4 Linux](http://repo.continuum.io/miniconda/Miniconda3-3.8.3-Linux-x86_64.sh), and this is the command you should run: `sh Miniconda3-3.8.3-Linux-x86_64.sh`
3. Make sure you have the latest version of conda: `conda update conda`
4. Now you have a full fledged version of `miniconda3` and `Python 3.4`, congrats!
5. Final step: Install packages. There are two options: If you have tons of space in your hard drive, go ahead and install anaconda. To do that, you need to run: `conda install anaconda`. This will install several [nice packages](http://docs.continuum.io/anaconda/pkg-docs.html) that are useful for machine learning. Option 2: Use `conda` or other installer to add packages as you need them. The syntax is `conda install packagename`.

