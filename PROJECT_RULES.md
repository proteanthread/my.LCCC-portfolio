# UNIVERSAL PROJECT RULES

> **Purpose**: This rulebook defines universal, project-agnostic engineering invariants, architectural standards, and resource safety guidelines that apply across all software projects, scripts, tools, and repositories. Every project inherits these universal invariants while maintaining its own domain-specific extensions.

---

## 0. Project Governance, User Primacy & Risk Advisory Invariants

### 0.1 User Primacy, Default Rule Adherence & Proactive Risk Advisory Invariant
* **User Primacy ("Whatever I say goes")**: The explicit instructions, architectural directives, design decisions, and overrides of the user supersede all established project rules, architectural conventions, style guidelines, and default invariants. Whatever the user directs is final and authoritative.
* **Default Rule Adherence ("If I don't say anything, follow the rules")**: In the absence of explicit user instructions, overrides, or alternative directions, the agent and developer MUST strictly and faithfully adhere to all rules, architectural invariants, memory models, quality gates, and verification standards defined within this document.
* **Proactive Risk Advisory & Deviation Warning ("Notify me and tell me why, but I decide")**: If an explicit user instruction, direction, or requested shortcut has the potential to break the project, introduce regressions, violate safety/memory bounds, cause architectural divergence, or stray from core project goals, the agent MUST proactively notify the user and clearly explain why before acting. However, risk disclosures are strictly informational and advisory: the user retains exclusive decision-making authority ("the user decides"). Once the user confirms their direction, the agent must proceed immediately and faithfully with the user's decision.

---

## 1. Resource, Memory & Traversal Safety Invariants

### 1.1 Anti-Buffering Streaming & Batch Traversal Invariant
* **Zero Unbounded Buffering**: Tools, scripts, crawlers, and algorithms MUST NEVER buffer unbounded collections (e.g., entire drives, multi-gigabyte directories, massive database dumps, or high-volume log streams) into monolithic in-memory arrays.
* **Bounded Streaming Pipelines**: Traversal and processing must execute using streaming iterators, chunked pipelines, or fixed-size batch cycles (e.g., 100 items per cycle) with deterministic progress feedback to the user.
* **Streaming Disk Persistence**: Catalogs, logs, audit trails, and manifest files must be streamed incrementally to disk as records are processed, rather than held in memory and written in bulk at completion.

### 1.2 Lazy Evaluation & Cost-Deferred Processing Invariant
* **Cost-Deferred Execution**: Computationally expensive operations (e.g., cryptographic SHA-256 hashing, deep binary parsing, remote network queries, image rendering, or full document deserialization) MUST NOT be executed upfront across all candidates.
* **On-Demand Resolution**: Defer expensive computations until conflict, collision, or explicit user requirement (e.g., "lazy hashing": verify destination slot availability first, and only compute full file hashes when an identical filename collision requires duplicate vs. unique disambiguation).
* **Early-Exit Filters**: Apply cheap, high-selectivity heuristics (file extension checks, file size comparisons, header signatures) before triggering heavy analytical pipelines.

### 1.3 Traversal Directory Pruning & Boundary Containment
* **Root-Level Pruning**: Filesystem traversals must prune destination trees, hidden directories, build output folders (`build*`, `dist`, `out`, `target`), version control trees (`.git`, `.svn`), dependency caches (`node_modules`, `vendor`, `.cache`), and virtual system volumes (`System Volume Information`, `$RECYCLE.BIN`, `/proc`, `/sys`) directly at the enumeration root rather than reading and filtering them in-flight.
* **Reparse Point & Loop Containment**: Symbolic links, directory junctions, and reparse points must be explicitly detected and ignored by default during recursive scans to prevent circular traversal, infinite recursion, and drive-wide disk thrashing.
* **Boundary Validation**: Before running any batch moving, sorting, or restructuring operation, verify that the destination directory is not identical to or nested within an active source traversal path unless explicitly designed with root-level exclusion guards.

### 1.4 Memory & Resource Integrity
* **Deterministic Resource Teardown**: Every allocated resource (file handles, sockets, mutexes, memory buffers, sub-processes) must have an unambiguous lifecycle and be released promptly in function epilogues, cleanup blocks (`finally`, `trap`, `goto cleanup`), or context managers.
* **Safe Growth & Bounds Checking**: Collection growth operations must validate integer bounds to prevent arithmetic overflow and memory exhaustion. Dynamic allocations must be zero-initialized upon creation.

### 1.5 Certified Memory Lifecycles & Bounded Resource Spectrum
* **Bounded Allocation Lifecycles**: All dynamic memory and resource allocations must belong to an explicit, bounded lifecycle (per-request, per-batch, monotonic arena, or scoped context manager). Unchecked, unbounded heap allocations that accumulate across loops without intermediate teardown are strictly prohibited.
* **Zero-Initialization Invariant**: All buffers, collections, structs, and objects must be zero-initialized or initialized to safe default states immediately upon allocation. Stack structures must be declared with `= {0}` (C) or default object constructors.
* **Safe Growth & Capacity Limits**: Dynamic collection growth must enforce strict upper capacity limits and validate integer arithmetic against overflow (`size_t` / integer wrap-around).

---

## 2. Architecture & Cross-Platform Engineering Invariants

### 2.1 Cross-Platform Dual-Implementation Lockstep Parity
* **100% Feature Parity**: When a project maintains multiple implementation platforms (e.g., Windows PowerShell 5.1/7+ and POSIX Bash 3.2+, or native C engine and Python SDK), all scripts, tools, and command-line interfaces MUST be developed, maintained, and updated in 100% parallel feature parity.
* **Synchronized Taxonomies & Behaviors**: Category names, CLI flags, default values, collision resolution algorithms, and output reports must match identically across platforms. No platform may lag in features, taxonomy updates, or bug fixes.
* **Platform API Isolation**: Platform-specific logic (Win32 P/Invoke, POSIX syscalls, OS-specific paths) must be encapsulated in designated abstraction layers. Core business logic, parsers, and data models must remain completely platform-agnostic.

### 2.2 Deterministic Token Disambiguation & Collision Shield
* **No Greedy or Ambiguous Tokens**: Tokenization and classification algorithms must strictly guard against greedy, ambiguous, or bare single-character tokens (e.g., a bare token `'C'` must never swallow-match 'Commodore 64', 'C16', or revision markers).
* **Boundary & Transition Analysis**: Keywords and tags must be matched using strict word boundary detection, transition analysis (letter-to-digit, digit-to-letter), and delimiter awareness (spaces, hyphens, underscores, slashes).
* **Nesting & Specificity Preference**: When multiple keywords or rules match a single input, longer and more specific matches must take precedence over generic or substring-nested matches (e.g., prefer 'Commodore 64' over 'Commodore').

### 2.3 Strict No-Stubs / No-Mocks Policy
* **Zero Placeholder Stubs**: Never introduce, prototype, or commit incomplete functions, mock handlers, empty endpoints, or no-op placeholder statements into the codebase. Every committed feature must be 100% operational and end-to-end verified.
* **Zero Technical Debt Inflation**: If a feature cannot be completely implemented and tested in the current development cycle, do not commit a partial stub. Defer the feature cleanly to avoid security vulnerabilities, untested code paths, and developer confusion.

### 2.4 Advanced Concurrency Ceilings & Worker Pool Limits
* **Hard Concurrency Ceilings**: Systems and scripts must NEVER spawn unbounded background threads, processes, or runspaces. All parallel execution must utilize fixed-size worker pools bounded by hardware capability ($\le \text{logical CPU cores}$).
* **Thread-Safe Data Synchronization**: Shared state across parallel workers must be protected via thread-safe queues, immutable messages, or synchronized locks to prevent data races and memory corruption.

### 2.5 Deterministic Async I/O Timeouts
* **Bounded Non-Blocking Operations**: All asynchronous network queries, inter-process communication (IPC) calls, and child process executions must enforce explicit, deterministic timeouts. Indefinite blocking on unverified sockets or pipes is strictly prohibited.

### 2.6 Catastrophic Backtracking Regex Shield
* **ReDoS Prevention**: Regular expression patterns must be designed and audited to eliminate catastrophic polynomial or exponential backtracking (avoiding nested quantifiers such as `(a+)+` or overlapping alternations).
* **Compile-Once Discipline**: Pre-compile regular expressions outside of hot processing loops rather than re-instantiating regex engines per record.

---

## 3. Testing, Verification & Maintenance Standards

### 3.1 Mandatory Expected-Results Assertion Testing Invariant
* **Assertion-Based Proof**: Never mark a feature, script, or bug fix as complete simply because the program ran or did not crash. Every modification MUST be proven with automated assertion-based test suites.
* **Exact Expected Values**: Tests must construct reproducible test fixtures, run the target pipeline, and assert actual runtime values, exit codes, output paths, and generated files against EXACT EXPECTED OUTPUTS (`Assert-Equal`, `assert_file_exists`, or `IF actual <> expected THEN FAIL`).
* **Multi-Platform Test Execution**: In multi-platform projects, automated test suites must exist and execute across all supported platforms (e.g., both `test.ps1` and `test_bash.sh`), with all assertions passing before work is finalized.

### 3.2 Synchronous-Only Scoped Cleanup Invariant
* **Zero Background Cleanups**: Build cleanup, test fixture removal, and intermediate artifact deletion MUST NEVER be launched as asynchronous background tasks. Cleanup operations must execute synchronously with bounded timeouts.
* **Scoped Targeting**: Cleanup utilities must strictly target designated intermediate directories and build trees (`build/`, `scratch/`, `test_run*`) rather than running unconstrained recursive file system scans across whole repositories.

### 3.3 Mandatory Headless Execution Protocol
* **Non-Interactive Batch Mode**: All automated tests, verification scripts, and CI/CD pipelines must execute with non-interactive flags (`--batch`, `-NonInteractive`, `--no-pause`, `--headless`) to eliminate REPL or stdin blocking.
* **Engine Execution Timeout**: Automated script executions must enforce bounded timeouts (e.g., `--timeout=15000` or process-level watchdogs) to prevent infinite loops from hanging sessions.

---

## 4. Project Extension Protocol

1. **Non-Destructive Local Augmentation**: Each individual repository's `PROJECT_RULES.md` inherits all universal rules in this document and supplements them with domain-specific sections (e.g., C17 compiler flags, CMake targets, dialect compatibility, or data pipeline schemas).
2. **Precedence Hierarchy**: Universal safety, resource, and verification invariants take precedence over local convenience hacks. Domain rules must conform to these universal standards.
3. **Continuous Synchronization**: When universal rules are updated, projects update their rule files via `project-rules-sync` without clobbering project-specific extensions.


---

## 5. Domain-Specific Project Rules & Architectural Extensions

> **Note**: Add project-specific rules, language specifications, compiler flags, and toolchain invariants below.
