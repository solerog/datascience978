<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 30 - ML Ops

## Train at scale

### Package

Reusable code.

- Can be shared

Hot reload on packages. NOT to use in production. If the package was already installed, it must be uninstalled previously.
It does not make a **copy**, but instances the actual package.

```py
pip install -e .
```

#### Testing

## Memory optimization

For large datasets, it may be useful to compress data bby 'downcasting' to the smallest possible values.
