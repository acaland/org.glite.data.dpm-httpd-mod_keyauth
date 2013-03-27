## This is the shared library to be built
lib_LTLIBRARIES = libmod_keyauth.la

## Define the source file for the module
libmod_keyauth_la_SOURCES = mod_keyauth.c
libmod_keyauth_la_LIBADD = -lssl

## Define that an include directory is required.
INCLUDES = -I/usr/kerberos/include @apache_includes@
CPPFLAGS = @apache_cppflags@
