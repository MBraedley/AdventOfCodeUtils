# Advent Of Code Utilities

This is a small utility library for solving common [Advent of Code](https://adventofcode.com/) puzzle types, written in C++

## Setup

This library is required for my Advent Of Code repos for 2025 and beyond.  `conan create` this package before using with the actual solutions package.

### Prerequisits

- [Python](https://www.python.org/)
- [Conan](https://conan.io/) - `pip install conan`
- [CMake](https://cmake.org/) - `pip install cmake`

### Dependencies

Dependencies are gathered with Conan from Conan Center.

- [CTRE](https://github.com/hanickadot/compile-time-regular-expressions)

### Build

Tested with Visual Studio 2022 Pro 17.14.21

```powershell
conan install .
conan create .
```

For editing, open the folder in Visual Studio and build solution.  **Do not regenerate the CMake cache** as this has broken my psuedo-solution in the past.
Letting Visual Studio do the normal CMake stuff is fine.  Calling `conan create` will be needed after edits in order for changes to be visible in the solutions package.
Alternatively, set the package as editable.  I _think_ this works, I haven't actually tried.

## Bugs and Issues

This library is fairly well tested through the use in prior AOC events.  It's unlikely there are any significant bugs.
