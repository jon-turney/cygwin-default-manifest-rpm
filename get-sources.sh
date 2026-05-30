#!
SPEC=${1:-cygwin-default-manifest.spec}
SRCDIR=${SRCDIR:-.}
version=$(rpmspec -q --qf '%{version}' --srpm ${SPEC})
REF=release-${version//./_}
git archive --prefix windows-default-manifest-${version}/ --output ${SRCDIR}/windows-default-manifest-${version}.tar.xz --remote git://cygwin.com/git/cygwin-apps/windows-default-manifest ${REF}
