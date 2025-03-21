Summary:	Generic USB CCID (Chip/Smart Card Interface Devices) driver
Summary(pl.UTF-8):	Ogólny sterownik USB CCID (Chip/Smart Card Interface Devices)
Name:		pcsc-driver-ccid
Version:	1.6.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://ccid.apdu.fr/files/ccid-%{version}.tar.xz
# Source0-md5:	c37cc9386e22928a23d87ff24b9e3097
URL:		https://ccid.apdu.fr/
BuildRequires:	flex
BuildRequires:	libusb-devel >= 1.0.9
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja
BuildRequires:	pcsc-lite-devel >= 1.8.3
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel >= 1.2.3.1
Requires:	libusb >= 1.0.9
Requires:	pcsc-lite >= 1.8.3
Provides:	ccid = %{version}-%{release}
Obsoletes:	ccid < 1.4.0-3
Obsoletes:	udev-pcsc-driver-ccid < 1.4.30
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		usbdropdir	/usr/%{_lib}/pcsc/drivers
%define		ccidtwindir	/usr/%{_lib}/pcsc/drivers/serial

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
%meson \
	--default-library=shared \
	-Dserial=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/udev/rules.d

%meson_install

cp -p src/92_pcscd_ccid.rules $RPM_BUILD_ROOT/lib/udev/rules.d/70-pcscd_ccid.rules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md SCARDGETATTRIB.md readers/supported_readers.txt
%dir %{usbdropdir}/ifd-ccid.bundle
%dir %{usbdropdir}/ifd-ccid.bundle/Contents
%{usbdropdir}/ifd-ccid.bundle/Contents/Info.plist
%dir %{usbdropdir}/ifd-ccid.bundle/Contents/Linux
%attr(755,root,root) %{usbdropdir}/ifd-ccid.bundle/Contents/Linux/libccid.so*
/lib/udev/rules.d/70-pcscd_ccid.rules

%files serial
%defattr(644,root,root,755)
%doc AUTHORS README.md SCARDGETATTRIB.md readers/supported_readers.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/reader.conf.d/libccidtwin
%dir %{ccidtwindir}
%attr(755,root,root) %{ccidtwindir}/libccidtwin.so*
