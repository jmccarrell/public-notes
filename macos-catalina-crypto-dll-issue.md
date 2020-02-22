# Description
In macos Catalina, Apple chose to tighten an access policy to loading dynamic libaries.

This has an effect on many systems we use at Sift, including:
- gsutils
- gcloud
- all Sift python scripts built against gcloud

# Am I affected?
Simple tests to see if your mac is affected:

## gsutil test
```
❯ gsutil ls gs://bigtable-prod.backup.sift.com/
/usr/local/bin/gsutil: line 193: 50575 Abort trap: 6           "$CLOUDSDK_GSUTIL_PYTHON" $CLOUDSDK_PYTHON_ARGS "${CLOUDSDK_ROOT_DIR}/bin/bootstrapping/gsutil.py" "$@"
```
## python test (2 or 3)
Type [these 5 lines](https://github.com/saltstack/salt/issues/55084#issuecomment-557162348) into a python shell

# What do I do to fix it?
Over time, the various software packages are getting updated, so you may not have to do anything.  But if you do, the general answer is to rely on the [Apple-supported dynamic link search path](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/UsingDynamicLibraries.html#//apple_ref/doc/uid/TP40002182-SW12) and put a versioned (link to a) copy of the two libs that have been causing problems so they will be found before the booby-trapped versions in `/usr/lib`.

The challenge is that you will be creating otherwise unmanaged symlinks to important dynamic link libraries; not generally a good idea, but it seems justified in this case.

## link versioned libs
The general recipe here is to symlink a recent version of the two crypto libs from a `homebrew` installed version of `openssl`.

So find what versions of `openssl` you have that are installed by `brew`:

```
❯ brew list | grep openssl
openssl
openssl@1.1
```

Prefer the unversioned one, so in this case `openssl`.   Then make some symlinks

```
cd /usr/local/lib
for l in libssl.dylib libcrypto.dylib; do ln -s $(brew --prefix openssl)/lib/$l $l; done
```

# What success looks like
After the fix, I see the expected:
## gsutil
```
❯ gsutil ls gs://bigtable-prod.backup.sift.com/
ServiceException: 401 Anonymous caller does not have storage.objects.list access to bigtable-prod.backup.sift.com.
```
## python
```
❯ python3
Python 3.7.6 (default, Dec 30 2019, 19:38:28)
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from ctypes.util import find_library
>>> lib = find_library('crypto')
>>> lib
'/usr/local/lib/libcrypto.dylib'
>>> from ctypes import cdll
>>> cdll.LoadLibrary(lib)
<CDLL '/usr/local/lib/libcrypto.dylib', handle 7f8a7f605f40 at 0x107f84550>
```
# Resources
- [Apple dynamic library search path](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/UsingDynamicLibraries.html#//apple_ref/doc/uid/TP40002182-SW12)
- [pip3 aborts immediately on Catalina Release version](https://github.com/Homebrew/homebrew-core/issues/44996#)
- [MacOS Catalina Abort Trap 6: requires cryptography >=2.8 or asn1crypto >= 1.0.0](https://github.com/pyca/pyopenssl/issues/874)
- [asn1crypto fails on macOS Catalina, due to loading unversioned /usr/lib/libcrypto.dylib](https://github.com/wbond/asn1crypto/issues/158)
- [salt fails on macOS Catalina, due to loading unversioned /usr/lib/libcrypto.dylib](https://github.com/saltstack/salt/issues/55084#)
