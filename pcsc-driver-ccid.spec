Summary:	Generic USB CCID (Chip/Smart Card Interface Devices) driver
Summary(pl.UTF-8):	Ogólny sterownik USB CCID (Chip/Smart Card Interface Devices)
Name:		pcsc-driver-ccid
Version:	1.3.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://alioth.debian.org/project/showfiles.php?group_id=30105
Source0:	http://alioth.debian.org/frs/download.php/2330/ccid-%{version}.tar.gz
# Source0-md5:	4bef11e5fb0ab6e2349936adb7a30cb8
URL:		http://pcsclite.alioth.debian.org/ccid.html
BuildRequires:	libusb-devel >= 0.1.7
BuildRequires:	pcsc-lite-devel >= 1.3.3
BuildRequires:	pkgconfig
Requires:	pcsc-lite >= 1.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		usbdropdir	/usr/%{_lib}/pcsc/drivers
%define		ccidtwindir	/usr/%{_lib}/pcsc/drivers

%description
This package provides generic USB CCID (Chip/Smart Card Interface
Devices) driver. Supported CCID readers:
- ActivCard USB reader 2.0
- Advanced Card Systems ACR 38U-CCID, ACR122
- Alcor Micro AU9520
- Athena: ASE IIIe USB v2, ASE IIIe KB USB
- Axalto Reflex USB v3
- Blutronics Bludrive II CCID 
- C3PO: LTC31, LTC32, TLTC2USB, KBR36
- Charismathics token
- Cherry: XX33, XX44, SmartTerminal ST2XX, ST-1044U, ST2000U,
  SmartBoard XX1X
- Dell: SK-3106 keyboard
- Eutron: SIM Pocket Combo, CryptoIdentity, Digipass 860, Smart Pocket
- Fujitsu Siemens Computers: SmartCard USB 2A, SmartCard Keyboard USB
  2A
- Gemplus: GemPC 433 SL, GemPC Card, GemPC Express, GemPC Key, GemPC
  PinPad, GemPC Twin, GemCore POS Pro, GemCore SIM Pro, Gem e-Seal Pro
- Giesecke & Devrient: CardToken 350, CardToken 550
- HP: USB Smart Card Keyboard, USB Smartcard Reader
- id3 Semiconductors: CL1356D, CL1356T
- Kobil: KAAN Base, KAAN Advanced, KAAN SIM III, mIDentity, SecOVID
  Reader III
- Lenovo Integrated Smart Card Reader
- O2Micro: Oz776, Oz7762
- OmniKey: CardMan 1021, CardMan 3021, CardMan 3121, CardMan 3621,
  CardMan 3821, CardMan 4321, CardMan 5121, CardMan 5125, CardMan 5321,
  CardMan 6121
- Philips JCOP41V221
- RSA SecurID SID800
- SCM Micro: SCR 331, SCR 331-DI, SCR 333, SCR 335, SCR 355, SCR 3310,
  SCR 3311, SCR 3320, SCR 3340, SPR 532, SDI 010
- SafeNet IKey4000
- SchlumbergerSema Cyberflex Access e-gate ICCD
- Silitek SK-3105 keyboard
- Sitecom MD-010 USB simcard reader
- SmartEpad v2.0
- Verisign: Secure Storage Token, Secure Token
- Winbond Electronics
- Xiring Teo

%description -l pl.UTF-8
Ten pakiet zawiera ogólny sterownik USB CCID (Chip/Smart Card
Interface Devices). Obsługiwane czytniki CCID:
- ActivCard USB reader 2.0
- Advanced Card Systems ACR 38U-CCID, ACR122
- Alcor Micro AU9520
- Athena: ASE IIIe USB v2, ASE IIIe KB USB
- Axalto Reflex USB v3
- Blutronics Bludrive II CCID 
- C3PO: LTC31, LTC32, TLTC2USB, KBR36
- Charismathics: token
- Cherry: XX33, XX44, SmartTerminal ST2XX, ST-1044U, ST2000U,
  SmartBoard XX1X
- Dell: klawiatura SK-3106
- Eutron: SIM Pocket Combo, CryptoIdentity, Digipass 860, Smart Pocket
- Fujitsu Siemens Computers: SmartCard USB 2A, SmartCard Keyboard USB
  2A
- Gemplus: GemPC 433 SL, GemPC Card, GemPC Express, GemPC Key, GemPC
  PinPad, GemPC Twin, GemCore POS Pro, GemCore SIM Pro, Gem e-Seal Pro
- Giesecke & Devrient: CardToken 350, CardToken 550
- HP: USB Smart Card Keyboard, USB Smartcard Reader
- id3 Semiconductors: CL1356D, CL1356T
- Kobil: KAAN Base, KAAN Advanced, KAAN SIM III, mIDentity, SecOVID
  Reader III
- Lenovo Integrated Smart Card Reader
- O2Micro: Oz776, Oz7762
- OmniKey: CardMan 1021, CardMan 3021, CardMan 3121, CardMan 3621,
  CardMan 3821, CardMan 4321, CardMan 5121, CardMan 5125, CardMan 5321,
  CardMan 6121
- Philips JCOP41V221
- RSA SecurID SID800
- SCM Micro: SCR 331, SCR 331-DI, SCR 333, SCR 335, SCR 355, SCR 3310,
  SCR 3311, SCR 3320, SCR 3340, SPR 532, SDI 010
- SafeNet IKey4000
- SchlumbergerSema Cyberflex Access e-gate ICCD
- Silitek: klawiatura SK-3105
- Sitecom: czytnik kart USB MD-010
- SmartEpad v2.0
- Verisign: Secure Storage Token, Secure Token
- Winbond Electronics
- Xiring Teo

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
	--enable-usbdropdir=%{usbdropdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C src install_ccidtwin \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sysconfdir}/reader.conf .

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
%attr(755,root,root) %{usbdropdir}/ifd-ccid.bundle/Contents/Linux/libccid.so.*.*.*
%{_mandir}/man1/RSA_SecurID_getpasswd.1*
%{_mandir}/man8/Kobil_mIDentity_switch.8*

%files serial
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README SCARDGETATTRIB.txt readers/GemPCTwin.txt readers/supported_readers.txt reader.conf
%attr(755,root,root) %{ccidtwindir}/libccidtwin.so.*
