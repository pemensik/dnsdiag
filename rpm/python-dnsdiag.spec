# Created by pyp2rpm-3.3.10
%global pypi_name dnsdiag
%global pypi_version 2.6.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        DNS Measurement, Troubleshooting and Security Auditing Toolset (ping, traceroute)

License:        BSD
URL:            https://dnsdiag.org/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
DNSDiag provides a handful of tools to measure and diagnose your DNS
performance and integrity. Using dnsping, dnstraceroute and dnseval tools you
can measure your DNS response quality from delay and loss perspective as well
as tracing the path your DNS query takes to get to DNS server.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aioquic) >= 1.2
Requires:       python3dist(cryptography) >= 42.0.5
Requires:       python3dist(cymruwhois) >= 1.6
Requires:       python3dist(dnspython) >= 2.7
Requires:       python3dist(h2) >= 4.1
Requires:       python3dist(httpx) >= 0.27
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
DNSDiag provides a handful of tools to measure and diagnose your DNS
performance and integrity. Using dnsping, dnstraceroute and dnseval tools you
can measure your DNS response quality from delay and loss perspective as well
as tracing the path your DNS query takes to get to DNS server.


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/dnseval
%{_bindir}/dnseval.py
%{_bindir}/dnsping
%{_bindir}/dnsping.py
%{_bindir}/dnstraceroute
%{_bindir}/dnstraceroute.py
%{python3_sitelib}/util
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
%autochangelog
