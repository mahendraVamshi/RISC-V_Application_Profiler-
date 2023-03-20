# RISC-V Application Profiler

This is a tool for profiling RISC-V applications.

## Installation

```shell
git clone https://github.com/mahendraVamshi/riscv-application-profiler.git
cd riscv-application-profiler
pip install -e .
```

## Usage

To display the help message, run:
```shell
riscv_application_profiler --help
riscv_application_profiler profile --help
```

To generate a log file, run:
```shell
spike --log-commits <path-to-binary>
```

**NOTE**: You need to use ``--enable-commitlog`` while configuring [spike](https://github.com/riscv-software-src/riscv-isa-sim#build-steps).

To profile an application, run:
```shell
riscv_application_profiler profile --log <path-to-log> --disass <path-to-disass> --output <path-to-output-file>
```

Command line arguements:

```text
-l, --log   [required]: Path to the log file generated by spike
-o --output [optional]: Path to the output file
```

Example:

```shell
riscv_application_profiler profile --log ./tests/hello.log --disass tests/hello.disass --output ./tests/hello.profile
```

**Note**: The log file should be an execution log generated using spike as of today. Support for configuring log formats will be added in the future.