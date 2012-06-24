Summary:	GNUe Designer - the IDE for the GNUe tools
Summary(pl):	GNUe Designer - IDE dla narz�dzi GNUe
Name:		gnue-designer
Version:	0.5.6
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.gnuenterprise.org/downloads/current/%{name}-%{version}.tar.gz
# Source0-md5:	04914daf8a846e0ac1b1e40d77077e29
URL:		http://www.gnuenterprise.org/
BuildRequires:	gnue-common
BuildRequires:	python
BuildRequires:	python-devel
Requires:	gnue-common
Requires:	python
Obsoletes:	GNUe-Designer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUe Designer is the IDE for the GNUe tools. It allows you to
visually layout your forms in a RAD-style environment. Designer has
a builtin forms client, so you can quickly test your forms while
still in Designer.  Designer also has support for form creation
wizards... answer a few questions, attach your form to one or more
database tables, select the fields to include, and, voila, a basic
form is created. Basic support for schema creation is also included.

%description -l pl
GNUe Designer to IDE (zintegrowane �rodowisko programistyczne) dla
narz�dzi GNUe. Pozwala na wizualne rozmieszczanie formularzy w
�rodowisku typu RAD. Designer ma wbudowanego klienta formularzy,
dzi�ki czemu mo�na szybko testowa� formularze z poziomu Designera.
Designer obs�uguje tak�e tworzenie formularzy za pomoc� wizard�w -
wystarczy odpowiedzie� na kilka pyta�, do��czy� formularz do jednej
lub wi�cej tabel bazy danych, wybra� pola do w��czenia i gotowe -
tworzony jest podstawowy formularz. Dost�pna jest te� podstawowa
obs�uga tworzenia schemat�w.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO doc/*.* doc/technotes
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/gnue/designer
%{_datadir}/gnue/images/designer
%{_mandir}/man?/*
