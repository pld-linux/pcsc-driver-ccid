Summary:	Generic USB CCID (Chip/Smart Card Interface Devices) driver
Summary(pl.UTF-8):	Ogólny sterownik USB CCID (Chip/Smart Card Interface Devices)
Name:		pcsc-driver-ccid
Version:	1.3.13
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://alioth.debian.org/project/showfiles.php?group_id=30105
Source0:	http://alioth.debian.org/frs/download.php/3300/ccid-%{version}.tar.bz2
# Source0-md5:	275360cb253299b763e1122adf847265
URL:		http://pcsclite.alioth.debian.org/ccid.html
BuildRequires:	libusb-devel >= 0.1.7
BuildRequires:	pcsc-lite-devel >= 1.5.3
BuildRequires:	pkgconfig
Requires:	pcsc-lite >= 1.5.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_check_so	1
%define		usbdropdir	/usr/%{_lib}/pcsc/drivers
%define		ccidtwindir	/usr/%{_lib}/pcsc/drivers

%description
This package provides generic USB CCID (Chip/Smart Card Interface
Devices) driver. Supported CCID readers:
- ActivCard: USB reader 3.0, Activkey Sim
- Advanced Card Systems ACR 38U-CCID, ACR122
- Alcor Micro AU9520
- Athena: ASE IIIe USB v2, ASE IIIe KB USB
- Axalto Reflex USB v3
- Blutronics Bludrive II CCID
- C3PO: LTC31, LTC32, TLTC2USB, KBR36
- Charismathics token
- Cherry: XX33, XX44, SmartTerminal ST2XX, ST-1044U, ST2000U,
  SmartBoard, G83-6610
- Covadis: Alya, Vega
- Dell: SK-3106 keyboard
- Eutron: SIM Pocket Combo, CryptoIdentity, Digipass 860, Smart Pocket
- Fujitsu Siemens Computers: SmartCard USB 2A, SmartCard Keyboard USB
  2A
- Gemplus/Gemalto: GemPC 433 SL, GemPC Card, GemPC Express, GemPC Key,
  GemPC PinPad, GemPC Twin, GemCore POS Pro, GemCore SIM Pro, Gem
  e-Seal Pro, USB Shell Token v2
- Giesecke & Devrient: CardToken 350, CardToken 550
- HP: USB Smart Card Keyboard, USB Smartcard Reader
- id3 Semiconductors: CL1356D, CL1356T, CL1356A HID
- Kobil: KAAN Base, KAAN Advanced, KAAN SIM III, KAAN TriB@nk, EMV
  TriCAP, mIDentity, SecOVID Reader III
- Lenovo Integrated Smart Card Reader
- Lexar/Gemalto Smart Enterprise Guardian
- O2Micro Oz776
- Oberthur ID-One Cosmo Card
- OmniKey: CardMan 1021, CardMan 3021, CardMan 3121, CardMan 3621,
  CardMan 3821, CardMan 4321, CardMan 5121, CardMan 5125, CardMan 5321,
  CardMan 6121
- Philips JCOP41V221
- Precise Biometrics 250 MC
- Pro-Active CSB6 Ultimate
- RSA SecurID SID800
- SCM Micro: SCR 331, SCR 331-DI, SCR 333, SCR 335, SCR 355, SCR 3310,
  SCR 3311, SCR 3320, SCR 3340, SPR 532, SDI 010
- SafeNet IKey4000
- SchlumbergerSema Cyberflex Access e-gate ICCD
- Silitek SK-3105 keyboard
- Sitecom MD-010 USB simcard reader
- SmartEpad v2.0
- Validy USB Token
- Vasco DP905
- Verisign: Secure Storage Token, Secure Token
- Winbond Electronics
- Xiring Teo

%description -l pl.UTF-8
Ten pakiet zawiera ogólny sterownik USB CCID (Chip/Smart Card
Interface Devices). Obsługiwane czytniki CCID:
- ActivCard USB reader 3.0
- Advanced Card Systems ACR 38U-CCID, ACR122
- Alcor Micro AU9520
- Athena: ASE IIIe USB v2, ASE IIIe KB USB
- Axalto Reflex USB v3
- Blutronics Bludrive II CCID
- C3PO: LTC31, LTC32, TLTC2USB, KBR36
- Charismathics: token
- Cherry: XX33, XX44, SmartTerminal ST2XX, ST-1044U, ST2000U,
  SmartBoard, G83-6610
- Covadis: Alya, Véga
- Dell: klawiatura SK-3106
- Eutron: SIM Pocket Combo, CryptoIdentity, Digipass 860, Smart Pocket
- Fujitsu Siemens Computers: SmartCard USB 2A, SmartCard Keyboard USB
  2A
- Gemplus/Gemalto: GemPC 433 SL, GemPC Card, GemPC Express, GemPC Key,
  GemPC PinPad, GemPC Twin, GemCore POS Pro, GemCore SIM Pro, Gem
  e-Seal Pro, USB Shell Token v2
- Giesecke & Devrient: CardToken 350, CardToken 550
- HP: USB Smart Card Keyboard, USB Smartcard Reader
- id3 Semiconductors: CL1356D, CL1356T, CL1356A HID
- Kobil: KAAN Base, KAAN Advanced, KAAN SIM III, KAAN TriB@nk, EMV
  TriCAP, mIDentity, SecOVID Reader III
- Lenovo Integrated Smart Card Reader
- Lexar/Gemalto Smart Enterprise Guardian
- O2Micro Oz776
- OmniKey: CardMan 1021, CardMan 3021, CardMan 3121, CardMan 3621,
  CardMan 3821, CardMan 4321, CardMan 5121, CardMan 5125, CardMan 5321,
  CardMan 6121
- Philips JCOP41V221
- Precise Biometrics 250 MC
- Pro-Active CSB6 Ultimate
- RSA SecurID SID800
- SCM Micro: SCR 331, SCR 331-DI, SCR 333, SCR 335, SCR 355, SCR 3310,
  SCR 3311, SCR 3320, SCR 3340, SPR 532, SDI 010
- SafeNet IKey4000
- SchlumbergerSema Cyberflex Access e-gate ICCD
- Silitek: klawiatura SK-3105
- Sitecom: czytnik kart USB MD-010
- SmartEpad v2.0
- Validy USB Token
- Vasco DP905
- Verisign: Secure Storage Token, Secure Token
- Winbond Electronics
- Xiring Teo

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
Requires:	pcsc-lite >= 1.3.3

%description serial
Generic USB CCID driver for readers connected to serial port.
Supported CCID readers:
- Gemplus GemPC Twin

%description serial -l pl.UTF-8
Ogólny sterownik USB CCID dla czytników podłączonych przez port
szeregowy. Obsługiwane czytniki CCID:
- Gemplus GemPC Twin

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
install -d $RPM_BUILD_ROOT/etc/udev/rules.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C src install_ccidtwin \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sysconfdir}/reader.conf .

install src/pcscd_ccid.rules $RPM_BUILD_ROOT/etc/udev/rules.d/70-pcscd_ccid.rules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README SCARDGETATTRIB.txt readers/*.txt contrib/Kobil_mIDentity_switch/README_Kobil_mIDentity_switch.txt
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
/etc/udev/rules.d/70-pcscd_ccid.rules

%files serial
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README SCARDGETATTRIB.txt readers/supported_readers.txt reader.conf
%attr(755,root,root) %{ccidtwindir}/libccidtwin.so*
