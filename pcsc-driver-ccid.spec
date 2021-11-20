Summary:	Generic USB CCID (Chip/Smart Card Interface Devices) driver
Summary(pl.UTF-8):	Ogólny sterownik USB CCID (Chip/Smart Card Interface Devices)
Name:		pcsc-driver-ccid
Version:	1.4.33
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://ccid.apdu.fr/files/ccid-%{version}.tar.bz2
# Source0-md5:	b11907894ce2d345439635e2b967e7e5
URL:		https://ccid.apdu.fr/
BuildRequires:	libusb-devel >= 1.0.9
BuildRequires:	pcsc-lite-devel >= 1.8.3
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.583
Requires:	libusb >= 1.0.9
Requires:	pcsc-lite >= 1.8.3
Provides:	ccid = %{version}-%{release}
Obsoletes:	ccid < 1.4.0-3
Obsoletes:	udev-pcsc-driver-ccid
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		usbdropdir	/usr/%{_lib}/pcsc/drivers
%define		ccidtwindir	/usr/%{_lib}/pcsc/drivers

# pcscd provides log_msg and log_xxd functions
%define		skip_post_check_so	libccid.so.1.4.0 libccidtwin.so.1.4.0

%description
This package provides generic USB CCID (Chip/Smart Card Interface
Devices) driver.

Full lists of supported devices are available here:
<https://ccid.apdu.fr/ccid/supported.html>
<https://ccid.apdu.fr/ccid/shouldwork.html>

%description -l pl.UTF-8
Ten pakiet zawiera ogólny sterownik USB CCID (Chip/Smart Card
Interface Devices).

Pełne listy obsługiwanych urządzeń są dostępne na WWW:
<https://ccid.apdu.fr/ccid/supported.html>
<https://ccid.apdu.fr/ccid/shouldwork.html>

%package serial
Summary:	Generic USB CCID driver for readers connected to serial port
Summary(pl.UTF-8):	Ogólny sterownik USB CCID dla czytników podłączonych przez port szeregowy
Group:		Libraries
Requires:	pcsc-lite >= 1.8.3

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
	--disable-silent-rules \
	--enable-ccidtwindir=%{ccidtwindir} \
	--enable-twinserial \
	--enable-usbdropdir=%{usbdropdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/udev/rules.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C src install_ccidtwin \
	DESTDIR=$RPM_BUILD_ROOT

cp -p src/92_pcscd_ccid.rules $RPM_BUILD_ROOT/lib/udev/rules.d/70-pcscd_ccid.rules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md SCARDGETATTRIB.txt readers/supported_readers.txt
%dir %{usbdropdir}/ifd-ccid.bundle
%dir %{usbdropdir}/ifd-ccid.bundle/Contents
%{usbdropdir}/ifd-ccid.bundle/Contents/Info.plist
%dir %{usbdropdir}/ifd-ccid.bundle/Contents/Linux
%attr(755,root,root) %{usbdropdir}/ifd-ccid.bundle/Contents/Linux/libccid.so*
/lib/udev/rules.d/70-pcscd_ccid.rules

%files serial
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md SCARDGETATTRIB.txt readers/supported_readers.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/reader.conf.d/libccidtwin
%attr(755,root,root) %{ccidtwindir}/libccidtwin.so*
