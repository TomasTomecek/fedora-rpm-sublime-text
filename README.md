# RPM of Sublime Text 3

## How to build

```
$ rpmbuild ./*.spec --define "_sourcedir ${PWD}" \
                    --define "_specdir ${PWD}" \
                    --define "_builddir ${PWD}" \
                    --define "_srcrpmdir ${PWD}" \
                    --define "_rpmdir ${PWD}" \
                    -bb
```

## How to install

```
$ sudo dnf install ./x86_64/sublime-text-*.x86_64.rpm
```
