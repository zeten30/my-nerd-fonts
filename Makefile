# RPM Makefile
RELEASE=30

srpm:
	./create-sources.sh
	mock -r fedora-$(RELEASE)-x86_64 --spec my-nerd-fonts.spec --sources sources --resultdir rpmbuild/ --buildsrpm

rpm: srpm
	mock -r fedora-$(RELEASE)-x86_64 --rebuild rpmbuild/my-nerd*.src.rpm --resultdir rpmbuild/

copr: srpm
	copr-cli build mzink/Utils rpmbuild/my-nerd-*.src.rpm --nowait

clean:
	rm -rf sources/* upstream/* rpmbuild/*