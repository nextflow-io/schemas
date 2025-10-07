# Pipeline Input Examples

This page provides practical examples of pipeline input schemas for various use cases.

## Basic Examples

### Minimal Schema

The simplest valid schema with only required properties:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/minimal-schema.json",
  "title": "Minimal Pipeline",
  "description": "Minimal valid pipeline schema",
  "type": "object"
}
```

### Simple Parameters

Basic parameter definitions:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/simple-params.json",
  "title": "Simple Parameters",
  "description": "Basic parameter types",
  "type": "object",
  "properties": {
    "input": {
      "type": "string",
      "format": "file-path",
      "description": "Input file path"
    },
    "output_dir": {
      "type": "string",
      "format": "directory-path",
      "description": "Output directory",
      "default": "./results"
    },
    "threads": {
      "type": "integer",
      "minimum": 1,
      "maximum": 32,
      "default": 4,
      "description": "Number of threads"
    },
    "verbose": {
      "type": "boolean",
      "description": "Enable verbose output",
      "default": false
    }
  }
}
```

## RNA-Seq Pipeline

Comprehensive RNA-Seq analysis pipeline schema:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://github.com/my-org/rnaseq-pipeline/schema.json",
  "title": "RNA-Seq Pipeline Parameters",
  "description": "Parameters for RNA sequencing analysis",
  "type": "object",
  "$defs": {
    "input_output_options": {
      "title": "Input/Output Options",
      "type": "object",
      "fa_icon": "fas fa-terminal",
      "description": "Define input data and output locations",
      "required": ["input", "outdir"],
      "properties": {
        "input": {
          "type": "string",
          "format": "file-path",
          "exists": true,
          "description": "Path to samplesheet CSV",
          "help_text": "CSV file with columns: sample,fastq_1,fastq_2,strandedness",
          "fa_icon": "fas fa-file-csv"
        },
        "outdir": {
          "type": "string",
          "format": "directory-path",
          "description": "Output directory",
          "default": "./results",
          "fa_icon": "fas fa-folder-open"
        }
      }
    },
    "reference_genome_options": {
      "title": "Reference Genome",
      "type": "object",
      "fa_icon": "fas fa-dna",
      "description": "Reference genome configuration",
      "properties": {
        "genome": {
          "type": "string",
          "description": "Reference genome name",
          "enum": ["GRCh38", "GRCh37", "GRCm39", "GRCm38"],
          "help_text": "Select a built-in reference genome"
        },
        "fasta": {
          "type": "string",
          "format": "file-path",
          "description": "Custom reference genome FASTA",
          "help_text": "Path to custom reference genome (overrides --genome)"
        },
        "gtf": {
          "type": "string",
          "format": "file-path",
          "description": "Custom GTF annotation file",
          "help_text": "Gene annotation in GTF format"
        }
      }
    },
    "alignment_options": {
      "title": "Alignment Options",
      "type": "object",
      "fa_icon": "fas fa-align-center",
      "description": "Read alignment parameters",
      "properties": {
        "aligner": {
          "type": "string",
          "enum": ["star", "hisat2"],
          "default": "star",
          "description": "RNA-seq aligner to use"
        },
        "min_mapping_quality": {
          "type": "integer",
          "minimum": 0,
          "maximum": 60,
          "default": 10,
          "description": "Minimum mapping quality score",
          "help_text": "Reads with mapping quality below this threshold will be filtered"
        }
      }
    },
    "quantification_options": {
      "title": "Quantification Options",
      "type": "object",
      "fa_icon": "fas fa-calculator",
      "description": "Gene/transcript quantification settings",
      "properties": {
        "pseudo_aligner": {
          "type": "string",
          "enum": ["salmon", "kallisto"],
          "default": "salmon",
          "description": "Pseudo-aligner for quantification"
        },
        "skip_quantification": {
          "type": "boolean",
          "default": false,
          "description": "Skip quantification step"
        }
      }
    },
    "quality_control_options": {
      "title": "Quality Control",
      "type": "object",
      "fa_icon": "fas fa-check-circle",
      "description": "Quality control parameters",
      "properties": {
        "skip_fastqc": {
          "type": "boolean",
          "default": false,
          "description": "Skip FastQC"
        },
        "skip_multiqc": {
          "type": "boolean",
          "default": false,
          "description": "Skip MultiQC report generation"
        }
      }
    },
    "resource_options": {
      "title": "Resource Options",
      "type": "object",
      "fa_icon": "fas fa-server",
      "description": "Computational resource settings",
      "properties": {
        "max_cpus": {
          "type": "integer",
          "minimum": 1,
          "default": 16,
          "description": "Maximum CPUs per process"
        },
        "max_memory": {
          "type": "string",
          "pattern": "^\\d+\\.(GB|MB)$",
          "default": "128.GB",
          "description": "Maximum memory per process",
          "examples": ["128.GB", "256.GB"]
        },
        "max_time": {
          "type": "string",
          "pattern": "^\\d+\\.(h|d)$",
          "default": "240.h",
          "description": "Maximum time per process",
          "examples": ["240.h", "10.d"]
        }
      }
    }
  },
  "allOf": [
    { "$ref": "#/$defs/input_output_options" },
    { "$ref": "#/$defs/reference_genome_options" },
    { "$ref": "#/$defs/alignment_options" },
    { "$ref": "#/$defs/quantification_options" },
    { "$ref": "#/$defs/quality_control_options" },
    { "$ref": "#/$defs/resource_options" }
  ]
}
```

## Variant Calling Pipeline

Genomic variant calling pipeline:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://github.com/my-org/variant-calling/schema.json",
  "title": "Variant Calling Pipeline",
  "description": "Parameters for variant calling from sequencing data",
  "type": "object",
  "$defs": {
    "input_output_options": {
      "title": "Input/Output Options",
      "type": "object",
      "required": ["input", "outdir"],
      "properties": {
        "input": {
          "type": "string",
          "format": "file-path-pattern",
          "description": "Input FASTQ files",
          "help_text": "Path to input files. Use wildcards like: 'data/*.fastq.gz'",
          "examples": ["data/*.fastq.gz", "samples/*_R{1,2}.fastq.gz"]
        },
        "outdir": {
          "type": "string",
          "format": "directory-path",
          "default": "./results",
          "description": "Output directory"
        },
        "publish_dir_mode": {
          "type": "string",
          "enum": ["symlink", "copy", "move"],
          "default": "copy",
          "description": "Method for publishing files to output directory"
        }
      }
    },
    "reference_options": {
      "title": "Reference Options",
      "type": "object",
      "required": ["reference"],
      "properties": {
        "reference": {
          "type": "string",
          "format": "file-path",
          "exists": true,
          "description": "Reference genome FASTA file"
        },
        "known_sites": {
          "type": "string",
          "format": "file-path",
          "description": "Known variant sites VCF for recalibration"
        }
      }
    },
    "variant_calling_options": {
      "title": "Variant Calling",
      "type": "object",
      "properties": {
        "caller": {
          "type": "string",
          "enum": ["gatk", "freebayes", "bcftools"],
          "default": "gatk",
          "description": "Variant calling tool"
        },
        "ploidy": {
          "type": "integer",
          "minimum": 1,
          "maximum": 4,
          "default": 2,
          "description": "Sample ploidy"
        },
        "min_base_quality": {
          "type": "integer",
          "minimum": 0,
          "maximum": 60,
          "default": 20,
          "description": "Minimum base quality score"
        }
      }
    },
    "filtering_options": {
      "title": "Filtering Options",
      "type": "object",
      "properties": {
        "min_depth": {
          "type": "integer",
          "minimum": 1,
          "default": 10,
          "description": "Minimum read depth"
        },
        "min_quality": {
          "type": "number",
          "minimum": 0,
          "default": 30.0,
          "description": "Minimum variant quality score"
        },
        "filter_low_qual": {
          "type": "boolean",
          "default": true,
          "description": "Filter low-quality variants"
        }
      }
    }
  },
  "allOf": [
    { "$ref": "#/$defs/input_output_options" },
    { "$ref": "#/$defs/reference_options" },
    { "$ref": "#/$defs/variant_calling_options" },
    { "$ref": "#/$defs/filtering_options" }
  ],
  "dependentRequired": {
    "known_sites": ["reference"]
  }
}
```

## Machine Learning Pipeline

Data processing and ML pipeline:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://github.com/my-org/ml-pipeline/schema.json",
  "title": "Machine Learning Pipeline",
  "description": "Parameters for ML model training pipeline",
  "type": "object",
  "$defs": {
    "data_options": {
      "title": "Data Options",
      "type": "object",
      "required": ["training_data"],
      "properties": {
        "training_data": {
          "type": "string",
          "format": "file-path",
          "exists": true,
          "description": "Training dataset"
        },
        "validation_data": {
          "type": "string",
          "format": "file-path",
          "description": "Validation dataset (optional)"
        },
        "test_data": {
          "type": "string",
          "format": "file-path",
          "description": "Test dataset (optional)"
        },
        "data_format": {
          "type": "string",
          "enum": ["csv", "parquet", "json"],
          "default": "csv",
          "description": "Input data format"
        }
      }
    },
    "preprocessing_options": {
      "title": "Preprocessing",
      "type": "object",
      "properties": {
        "normalize": {
          "type": "boolean",
          "default": true,
          "description": "Normalize features"
        },
        "impute_missing": {
          "type": "boolean",
          "default": true,
          "description": "Impute missing values"
        },
        "feature_selection": {
          "type": "string",
          "enum": ["none", "variance", "mutual_info", "rfe"],
          "default": "none",
          "description": "Feature selection method"
        }
      }
    },
    "model_options": {
      "title": "Model Options",
      "type": "object",
      "properties": {
        "model_type": {
          "type": "string",
          "enum": ["random_forest", "xgboost", "neural_network", "svm"],
          "default": "random_forest",
          "description": "Model architecture"
        },
        "random_seed": {
          "type": "integer",
          "minimum": 0,
          "default": 42,
          "description": "Random seed for reproducibility"
        },
        "n_estimators": {
          "type": "integer",
          "minimum": 1,
          "default": 100,
          "description": "Number of estimators (tree-based models)"
        },
        "learning_rate": {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 1,
          "default": 0.01,
          "description": "Learning rate"
        }
      }
    },
    "training_options": {
      "title": "Training Options",
      "type": "object",
      "properties": {
        "epochs": {
          "type": "integer",
          "minimum": 1,
          "default": 100,
          "description": "Training epochs"
        },
        "batch_size": {
          "type": "integer",
          "minimum": 1,
          "multipleOf": 2,
          "default": 32,
          "description": "Batch size (power of 2 recommended)"
        },
        "early_stopping": {
          "type": "boolean",
          "default": true,
          "description": "Enable early stopping"
        },
        "patience": {
          "type": "integer",
          "minimum": 1,
          "default": 10,
          "description": "Early stopping patience"
        }
      }
    }
  },
  "allOf": [
    { "$ref": "#/$defs/data_options" },
    { "$ref": "#/$defs/preprocessing_options" },
    { "$ref": "#/$defs/model_options" },
    { "$ref": "#/$defs/training_options" }
  ]
}
```

## Advanced Features

### Conditional Requirements

Parameters that depend on other parameters:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/conditional.json",
  "title": "Conditional Requirements",
  "description": "Parameters with dependencies",
  "type": "object",
  "properties": {
    "use_cache": {
      "type": "boolean",
      "description": "Enable caching"
    },
    "cache_dir": {
      "type": "string",
      "format": "directory-path",
      "description": "Cache directory"
    },
    "enable_logging": {
      "type": "boolean",
      "description": "Enable logging"
    },
    "log_file": {
      "type": "string",
      "format": "file-path",
      "description": "Log file path"
    }
  },
  "dependentRequired": {
    "use_cache": ["cache_dir"],
    "enable_logging": ["log_file"]
  }
}
```

### Custom Error Messages

Helpful error messages for validation failures:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/error-messages.json",
  "title": "Custom Error Messages",
  "description": "Parameters with custom validation messages",
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "format": "email",
      "description": "Notification email",
      "errorMessage": "Please provide a valid email address for notifications"
    },
    "memory": {
      "type": "string",
      "pattern": "^\\d+\\.(GB|MB)$",
      "description": "Memory allocation",
      "errorMessage": "Memory must be specified with units, e.g., '8.GB' or '512.MB'"
    },
    "threads": {
      "type": "integer",
      "minimum": 1,
      "maximum": 64,
      "description": "Thread count",
      "errorMessage": "Thread count must be between 1 and 64"
    }
  }
}
```

### Deprecated Parameters

Marking parameters as deprecated:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/deprecated.json",
  "title": "Deprecated Parameters",
  "description": "Schema with deprecated options",
  "type": "object",
  "properties": {
    "output_format": {
      "type": "string",
      "enum": ["json", "yaml", "csv"],
      "description": "Output format"
    },
    "outfmt": {
      "type": "string",
      "description": "Legacy output format parameter",
      "deprecated": true,
      "errorMessage": "The 'outfmt' parameter is deprecated. Please use 'output_format' instead."
    }
  }
}
```

## See Also

- [Pipeline Input Schema Reference](../schemas/pipeline-input.md)
- [Quick Start Guide](../getting-started/quick-start.md)
- [Testing Guide](../development/testing.md)
