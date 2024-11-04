#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-fastICA
Version  : 1.2.5.1
Release  : 58
URL      : https://cran.r-project.org/src/contrib/fastICA_1.2-5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fastICA_1.2-5.1.tar.gz
Summary  : FastICA Algorithms to Perform ICA and Projection Pursuit
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-fastICA-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Component Analysis (ICA) and Projection Pursuit.

%package lib
Summary: lib components for the R-fastICA package.
Group: Libraries

%description lib
lib components for the R-fastICA package.


%prep
%setup -q -n fastICA
pushd ..
cp -a fastICA buildavx2
popd
pushd ..
cp -a fastICA buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724249402

%install
export SOURCE_DATE_EPOCH=1724249402
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fastICA/DESCRIPTION
/usr/lib64/R/library/fastICA/HISTORY
/usr/lib64/R/library/fastICA/INDEX
/usr/lib64/R/library/fastICA/Meta/Rd.rds
/usr/lib64/R/library/fastICA/Meta/features.rds
/usr/lib64/R/library/fastICA/Meta/hsearch.rds
/usr/lib64/R/library/fastICA/Meta/links.rds
/usr/lib64/R/library/fastICA/Meta/nsInfo.rds
/usr/lib64/R/library/fastICA/Meta/package.rds
/usr/lib64/R/library/fastICA/NAMESPACE
/usr/lib64/R/library/fastICA/R/fastICA
/usr/lib64/R/library/fastICA/R/fastICA.rdb
/usr/lib64/R/library/fastICA/R/fastICA.rdx
/usr/lib64/R/library/fastICA/README
/usr/lib64/R/library/fastICA/help/AnIndex
/usr/lib64/R/library/fastICA/help/aliases.rds
/usr/lib64/R/library/fastICA/help/fastICA.rdb
/usr/lib64/R/library/fastICA/help/fastICA.rdx
/usr/lib64/R/library/fastICA/help/paths.rds
/usr/lib64/R/library/fastICA/html/00Index.html
/usr/lib64/R/library/fastICA/html/R.css
/usr/lib64/R/library/fastICA/tests/one-component.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/fastICA/libs/fastICA.so
/V4/usr/lib64/R/library/fastICA/libs/fastICA.so
/usr/lib64/R/library/fastICA/libs/fastICA.so
