%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 0
%global with_bundled 1
%global with_debug 0
%global with_check 1
%global with_unit_test 0
%else
%global with_devel 0
%global with_bundled 1
%global with_debug 0
%global with_check 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider github
%global provider_tld com
%global project coreos
%global repo rkt

%global git0 https://%{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit0 8f74d2895a6a3bbf78edd99bcd9104c0257d9862
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# valid values: coreos usr-from-src usr-from-host
%global stage1_flavors host

Name: %{repo}
Version: 1.6.0
Release: 4.git%{shortcommit0}%{?dist}
Summary: CLI for running app containers
License: ASL 2.0
URL: https://%{import_path}
ExclusiveArch: x86_64
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bc
BuildRequires: glibc-static
BuildRequires: golang >= 1.6
BuildRequires: gperf
BuildRequires: gnupg
BuildRequires: intltool
BuildRequires: libacl-devel
BuildRequires: libcap-devel
BuildRequires: libgcrypt-devel
BuildRequires: libtool
BuildRequires: libmount-devel
BuildRequires: libxkbcommon-devel
BuildRequires: trousers-devel
BuildRequires: perl-Config-Tiny
BuildRequires: squashfs-tools
BuildRequires: systemd >= 222

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(camlistore.org/pkg/legal)
BuildRequires: golang(github.com/coreos/etcd/client)
BuildRequires: golang(github.com/appc/cni/pkg/invoke)
BuildRequires: golang(github.com/appc/cni/pkg/ip)
BuildRequires: golang(github.com/appc/cni/pkg/ns)
BuildRequires: golang(github.com/appc/cni/pkg/types)
BuildRequires: golang(github.com/appc/docker2aci/lib/backend/file)
BuildRequires: golang(github.com/appc/docker2aci/lib/backend/repository)
BuildRequires: golang(github.com/appc/docker2aci/lib/common)
BuildRequires: golang(github.com/appc/docker2aci/lib/types)
BuildRequires: golang(github.com/appc/docker2aci/lib/util)
BuildRequires: golang(github.com/appc/docker2aci/tarball)
BuildRequires: golang(github.com/appc/spec/aci)
BuildRequires: golang(github.com/appc/spec/pkg/acirenderer)
BuildRequires: golang(github.com/appc/spec/pkg/device)
BuildRequires: golang(github.com/appc/spec/pkg/tarheader)
BuildRequires: golang(github.com/appc/spec/schema)
BuildRequires: golang(github.com/appc/spec/schema/common)
BuildRequires: golang(github.com/appc/spec/schema/types)
BuildRequires: golang(github.com/bradfitz/http2)
BuildRequires: golang(github.com/bradfitz/http2/hpack)
BuildRequires: golang(github.com/camlistore/camlistore/pkg/errorutil)
BuildRequires: golang(github.com/camlistore/lock)
BuildRequires: golang(github.com/coreos/go-iptables/iptables)
BuildRequires: golang(github.com/coreos/go-semver/semver)
BuildRequires: golang(github.com/coreos/go-tspi/attestation)
BuildRequires: golang(github.com/coreos/go-tspi/tspi)
BuildRequires: golang(github.com/coreos/ioprogress)
BuildRequires: golang(github.com/cpuguy83/go-md2man/md2man)
BuildRequires: golang(github.com/cznic/b)
BuildRequires: golang(github.com/cznic/bufs)
BuildRequires: golang(github.com/cznic/exp/lldb)
BuildRequires: golang(github.com/cznic/fileutil)
BuildRequires: golang(github.com/cznic/fileutil/falloc)
BuildRequires: golang(github.com/cznic/fileutil/storage)
BuildRequires: golang(github.com/cznic/mathutil)
BuildRequires: golang(github.com/cznic/ql)
BuildRequires: golang(github.com/cznic/sortutil)
BuildRequires: golang(github.com/cznic/strutil)
BuildRequires: golang(github.com/cznic/zappy)
BuildRequires: golang(github.com/d2g/dhcp4)
BuildRequires: golang(github.com/godbus/dbus)
BuildRequires: golang(github.com/godbus/dbus/introspect)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/proto/testdata)
BuildRequires: golang(github.com/gorilla/context)
BuildRequires: golang(github.com/inconshreveable/mousetrap)
BuildRequires: golang(github.com/kballard/go-shellquote)
BuildRequires: golang(github.com/kr/pty)
BuildRequires: golang(github.com/petar/GoLLRB/llrb)
BuildRequires: golang(github.com/russross/blackfriday)
BuildRequires: golang(github.com/shurcooL/sanitized_anchor_name)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/vishvananda/netlink)
BuildRequires: golang(github.com/vishvananda/netlink/nl)
BuildRequires: golang(golang.org/x/crypto/cast5)
BuildRequires: golang(golang.org/x/crypto/openpgp/armor)
BuildRequires: golang(golang.org/x/crypto/openpgp/elgamal)
BuildRequires: golang(golang.org/x/crypto/openpgp/errors)
BuildRequires: golang(golang.org/x/crypto/openpgp/packet)
BuildRequires: golang(golang.org/x/crypto/openpgp/s2k)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)
BuildRequires: golang(golang.org/x/net/internal/timeseries)
BuildRequires: golang(golang.org/x/net/trace)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/tools/go/vcs)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/benchmark/grpc_testing)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/grpclog)
BuildRequires: golang(google.golang.org/grpc/health/grpc_health_v1alpha)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(google.golang.org/grpc/naming)
BuildRequires: golang(google.golang.org/grpc/transport)
BuildRequires: golang(k8s.io/kubernetes/pkg/api/resource)
BuildRequires: golang(speter.net/go/exp/math/dec/inf)
BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/remyoudompheng/bigfft)
BuildRequires: golang(github.com/spf13/viper)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/oauth2/jwt)
BuildRequires: golang(golang.org/x/text/encoding)
BuildRequires: golang(golang.org/x/text/encoding/charmap)
BuildRequires: golang(golang.org/x/text/encoding/japanese)
BuildRequires: golang(golang.org/x/text/encoding/korean)
BuildRequires: golang(golang.org/x/text/encoding/simplifiedchinese)
BuildRequires: golang(golang.org/x/text/encoding/traditionalchinese)
BuildRequires: golang(golang.org/x/text/encoding/unicode)
BuildRequires: golang(golang.org/x/text/transform)
%endif

Requires(pre): shadow-utils
Requires(post): systemd >= 222
Requires(preun): systemd >= 222
Requires(postun): systemd >= 222

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary: %{summary}
BuildArch: noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif

%description devel
%{summary}

This package contains library source intended for building other packages
which use import path with %{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary: Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires: %{name}-devel = %{version}-%{release}

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{name}-%{commit0}

%build
./autogen.sh
# ./configure flags: https://github.com/coreos/rkt/blob/master/Documentation/build-configure.md
./configure --with-stage1-flavors=%{stage1_flavors} \
            --with-stage1-flavors-version-override=%{version}-%{release} \
            --with-stage1-default-location=%{_libexecdir}/%{name}/stage1-host.aci
GOPATH=$GOPATH:%{gopath}:$(pwd)/Godeps/_workspace make all bash-completion

%install
# install binaries
install -dp %{buildroot}{%{_bindir},%{_libexecdir}/%{name},%{_unitdir}}
install -dp %{buildroot}%{_sharedstatedir}/%{name}

install -p -m 755 build-%{name}-%{version}+git/bin/%{name} %{buildroot}%{_bindir}
install -p -m 755 dist/scripts/setup-data-dir.sh %{buildroot}%{_bindir}/%{name}-setup-data-dir.sh
install -p -m 644 build-%{name}-%{version}+git/bin/stage1-host.aci %{buildroot}%{_libexecdir}/%{name}

# install bash completion
install -dp %{buildroot}%{_datadir}/bash-completion/completions
install -p -m 644 dist/bash_completion/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

# install metadata unitfiles
install -p -m 644 dist/init/systemd/%{name}-gc.timer %{buildroot}%{_unitdir}
install -p -m 644 dist/init/systemd/%{name}-gc.service %{buildroot}%{_unitdir}
install -p -m 644 dist/init/systemd/%{name}-metadata.socket %{buildroot}%{_unitdir}
install -p -m 644 dist/init/systemd/%{name}-metadata.service %{buildroot}%{_unitdir}

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/Godeps/_workspace:%{gopath}
%endif
%endif

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
exit 0

%post
%{_bindir}/%{name}-setup-data-dir.sh
%systemd_post %{name}-metadata.service

%preun
%systemd_preun %{name}-metadata.service

%postun
%systemd_postun_with_restart %{name}-metadata.service

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTING.md DCO README.md Documentation/*
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc CONTRIBUTING.md DCO README.md Documentation/*
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md DCO README.md Documentation/*
%{_bindir}/%{name}
%{_bindir}/%{name}-setup-data-dir.sh
%{_libexecdir}/%{name}/stage1-host.aci
%{_unitdir}/%{name}*
%{_datadir}/bash-completion/completions/%{name}
%{_sharedstatedir}/%{name}

%changelog
* Tue May 24 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.6.0-4.git8f74d28
- built commit#8f74d28
