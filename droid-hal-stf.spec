# These and other macros are documented in dhd/droid-hal-device.inc
%define device stf
%define vendor honor

%define vendor_pretty Honor
%define device_pretty 9

%define droid_target_aarch64 1

%define installable_zip 1

%define straggler_files \
/bugreports \
/cache \
/d \
/file_contexts.bin \
/property_contexts \
/sdcard \
/selinux_version \
/service_contexts \
/vendor \
%{nil}


%include rpm/dhd/droid-hal-device.inc
