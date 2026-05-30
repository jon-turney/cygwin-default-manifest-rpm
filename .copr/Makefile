srpm:
	dnf -y install git rpmdevtools
	rpmdev-setuptree
	export SRCDIR=$$(rpm --eval "%{_sourcedir}") && \
	sh -x ./get-sources.sh $(spec)
	rpmbuild -bs $(spec)
	SRPMDIR=$$(rpm --eval "%{_srcrpmdir}") && \
	mv -v $${SRPMDIR}/* $(outdir)
