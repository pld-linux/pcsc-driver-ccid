Summary:	Generic USB CCID (Chip/Smart Card Interface Devices) driver
Summary(pl.UTF-8):	Ogólny sterownik USB CCID (Chip/Smart Card Interface Devices)
Name:		pcsc-driver-ccid
Version:	1.4.0
Release:	4
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://alioth.debian.org/project/showfiles.php?group_id=30105
Source0:	http://alioth.debian.org/frs/download.php/3333/ccid-%{version}.tar.bz2
# Source0-md5:	745d681bed2e17579fa6144e19bcb01d
URL:		http://pcsclite.alioth.debian.org/ccid.html
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	pcsc-lite-devel >= 1.6.2
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.583
Requires:	pcsc-lite >= 1.6.2
Provides:	ccid = %{version}-%{release}
Obsoletes:	ccid < 1.4.0-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		usbdropdir	/usr/%{_lib}/pcsc/drivers
%define		ccidtwindir	/usr/%{_lib}/pcsc/drivers

# pcscd provides log_msg and log_xxd functions
%define		skip_post_check_so	libccid.so.1.4.0 libccidtwin.so.1.4.0

%description
This package provides generic USB CCID (Chip/Smart Card Interface
Devices) driver.

Full lists of supported devices are available here:
<http://pcsclite.alioth.debian.org/supported.html>
<http://pcsclite.alioth.debian.org/shouldwork.html>

%description -l pl.UTF-8
Ten pakiet zawiera ogólny sterownik USB CCID (Chip/Smart Card
Interface Devices).

Pełne listy obsługiwanych urządzeń są dostępne na WWW:
<http://pcsclite.alioth.debian.org/supported.html>
<http://pcsclite.alioth.debian.org/shouldwork.html>

%package -n udev-pcsc-driver-ccid
Summary:	udev support for CCID PC/SC driver
Summary(pl.UTF-8):	Obsługa udev dla sterownika PC/SC CCID
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	udev-core

%description -n udev-pcsc-driver-ccid
udev support for CCID PC/SC driver.

%description -n udev-pcsc-driver-ccid -l pl.UTF-8
Obsługa udev dla sterownika PC/SC CCID.

%package serial
Summary:	Generic USB CCID driver for readers connected to serial port
Summary(pl.UTF-8):	Ogólny sterownik USB CCID dla czytników podłączonych przez port szeregowy
Group:		Libraries
Requires:	pcsc-lite >= 1.6.2

%description serial
Generic USB CCID driver for readers connected to serial port.
Supported CCID devices:
- Gemplus/Gemalto GemPC Twin
- Gemplus/Gemalto GemCore POS Pro
- Gemplus/Gemalto GemCore SIM Pro
- Gemalto GemPC PinPad

%description serial -l pl.UTF-8
Ogólny sterownik USB CCID dla czytników podłączonych przez port
szeregowy. Obsługiwane urządzenia CCID:
- Gemplus/Gemalto GemPC Twin
- Gemplus/Gemalto GemCore POS Pro
- Gemplus/Gemalto GemCore SIM Pro
- Gemalto GemPC PinPad

%prep
%setup -q -n ccid-%{version}

%build
%configure \
	--enable-ccidtwindir=%{ccidtwindir} \
	--enable-twinserial \
	--enable-usbdropdir=%{usbdropdir} \
	--enable-udev
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/udev/rules.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C src install_ccidtwin \
	DESTDIR=$RPM_BUILD_ROOT

cp -p src/pcscd_ccid.rules $RPM_BUILD_ROOT/lib/udev/rules.d/70-pcscd_ccid.rules

rm $RPM_BUILD_ROOT%{_docdir}/ccid/README_Kobil_mIDentity_switch.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README SCARDGETATTRIB.txt readers/supported_readers.txt contrib/Kobil_mIDentity_switch/README_Kobil_mIDentity_switch.txt
%attr(755,root,root) %{_bindir}/RSA_SecurID_getpasswd
%attr(755,root,root) %{_sbindir}/Kobil_mIDentity_switch
%dir %{usbdropdir}/ifd-ccid.bundle
%dir %{usbdropdir}/ifd-ccid.bundle/Contents
%{usbdropdir}/ifd-ccid.bundle/Contents/Info.plist
%dir %{usbdropdir}/ifd-ccid.bundle/Contents/Linux
%attr(755,root,root) %{usbdropdir}/ifd-ccid.bundle/Contents/Linux/libccid.so*
%{_mandir}/man1/RSA_SecurID_getpasswd.1*
%{_mandir}/man8/Kobil_mIDentity_switch.8*

%files -n udev-pcsc-driver-ccid
%defattr(644,root,root,755)
/lib/udev/rules.d/70-pcscd_ccid.rules

%files serial
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README SCARDGETATTRIB.txt readers/supported_readers.txt
%config(noreplace) %verify(not md5 mtime size) /etc/reader.conf.d/libccidtwin
%attr(755,root,root) %{ccidtwindir}/libccidtwin.so*
