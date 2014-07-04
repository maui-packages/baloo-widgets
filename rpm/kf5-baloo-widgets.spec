# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kf5-baloo-widgets

# >> macros
# << macros

Summary:    A Tier 3 KDE Frameworks 5 module that provides widgets built on top of Baloo
Version:    5.0.0
Release:    1
Group:      System/Base
License:    LGPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kf5-baloo-widgets.yaml
Source101:  kf5-baloo-widgets-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  libxapian-devel
BuildRequires:  kf5-kfilemetadata-devel
BuildRequires:  kf5-baloo-devel
BuildRequires:  kf5-umbrella

%description
A Tier 3 KDE Frameworks 5 module that provides widgets built on top of Baloo.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_kf5_libdir}/*.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_libdir}/*.so
%{_kf5_libdir}/cmake/KF5BalooWidgets
%{_kf5_includedir}/BalooWidgets
# >> files devel
# << files devel
