# UNIVERSAL AGENT BEHAVIORAL RULES & ARCHITECTURAL GUIDELINES

> **Purpose**: This rulebook defines project-agnostic behavioral guardrails, task execution safeguards, and operational invariants for AI coding agents operating across any codebase or workspace. Individual projects inherit these guidelines in their `.agents/AGENTS.md` alongside project-specific workflow rules.

---

## 0. User Primacy, Default Rule Adherence & Risk Advisory Guardrail

### 0.1 User Primacy, Default Rule Adherence & Proactive Risk Advisory Guardrail
* **User Primacy ("Whatever I say goes")**: The user's explicit instructions, commands, and design decisions take absolute precedence over all rulebooks, operating guidelines, and default agent behaviors. Whatever the user directs is the governing authority.
* **Default Rule Adherence ("If I don't say anything, follow the rules")**: When the user provides a task without specific procedural overrides or deviations, the agent MUST default to strict compliance with all project and agent operational rules.
* **Proactive Risk Advisory & Deviation Warning ("Notify me and tell me why, but I decide")**: If the user gives an instruction or makes a request that carries potential to break the build, cause functional or performance regressions, violate safety/memory constraints, compromise architectural integrity, or cause the project to stray, the agent has a mandatory duty to alert the user immediately. The agent must clearly and concisely explain the specific risks and why they could destabilize the project.
* **User Decision Authority**: Risk notifications are strictly informational and advisory. The agent must never refuse an explicit user instruction, engage in dogmatic resistance, or block execution once the risk has been communicated. The user makes the final decision ("the user decides"). When the user acknowledges or reaffirms their directive, the agent must execute it cleanly and without hesitation.

---

## 1. Background Execution, Inactivity & Clarification Safeguards

### 1.1 Zero Simulated Notifications
* **Absolute Invariant**: Agents MUST NOT simulate, fake, or manually output synthetic system or tool notification messages (such as faking a task completion message or mocking a timer event). All notifications must originate strictly from the runtime environment.

### 1.2 Mandatory Companion Watchdog Pairing
* **Watchdog Pairing Invariant**: An agent MUST NEVER launch an asynchronous background command (`run_command` going async) without immediately scheduling a companion one-shot watchdog timer via the `schedule` tool (e.g. `DurationSeconds="120"`, `TimerCondition="any"` or targeting the specific Task ID).
* **Watchdog Response Protocol**: If a companion watchdog timer fires or if a background task has shown no progress within its expected window, the agent MUST proactively probe task status (`manage_task(Action="status")`), inspect log files, and evaluate whether the task is progressing normally.

### 1.3 Zero Unbounded Inactivity
* **Active Progress Obligation**: Agents MUST NEVER yield execution into indefinite, unbounded silent waiting. While tight polling loops remain prohibited, the agent must ensure that every background task has an active watchdog or bounded termination condition.
* **Deadlock & Hang Prevention**: If a background task is detected in an unrecoverable, stalled, or failed state, the agent must immediately cancel it (`manage_task(Action="kill")`), analyze logs, and proceed with remediation.

### 1.4 Defensive Early-Termination Checks
* **Bounded Synchronous Execution**: For compilation, test runs, and CLI operations, prefer bounded synchronous execution (`WaitMsBeforeAsync` between 5,000ms and 60,000ms).
* **Immediate Exit-Code Triage**: If a command errors or terminates in sub-second time, the agent must immediately inspect exit codes and stderr/stdout rather than assuming healthy background execution.

### 1.5 Mandatory Sequential Clarification Gate & Zero-Assumption Discipline
* **Mandatory Clarification Gate**: When user requests involve underspecified requirements, architectural choices, or multiple viable implementations, agents MUST pause and conduct an interactive interview before generating implementation code or making irreversible changes.
* **High-Impact Question Filter (Anti-Pro-Forma Invariant)**: Agents MUST NOT ask questions merely to be thorough. Ask ONLY questions whose answers could change the recommendation, design, or implementation. If an architectural dimension, requirement, or convention is already clear or determined from code inspection, do not ask about it.
* **Sequential Branching Prioritization**: Ask clarifying questions one at a time, strictly prioritizing high-impact decisions whose answers alter the architecture or recommendation tree. If decisions are tightly coupled, structured multi-choice options may be presented together.
* **Unbounded Clarification Depth**: Agents must not artificially truncate clarification to arbitrary caps (e.g. 3 or 5 questions) if key architectural dependencies remain unresolved. Continue asking high-value questions until full alignment is achieved.
* **Transparent Recommendation Framing (Anti-Dogmatism)**: Agents MUST NOT present their preferred answer, design choice, or implementation strategy as though it were an objective fact. Always explicitly label preferred options as a recommendation (e.g., prefixing with `(Recommended)`, "Recommended approach:", or "Our recommendation is..."). Clearly differentiate between verifiable empirical facts (e.g. compiler errors, syntax rules, hardware limits) and recommended architectural choices.
* **Strict Zero-Assumption Invariant**: Agents must NEVER assume user preferences, target directories, or implementation scope when ambiguity exists.

### 1.6 Pre-Implementation 7-Dimension Interview Protocol & Plan Gate
* **7 Core Architectural Dimensions**: When planning non-trivial changes, agents must analyze the problem space across the 7 Core Dimensions:
  1. **Requirements**: Functional scope, user constraints, boundary conditions, and acceptance criteria.
  2. **Existing Behavior**: Current operational baseline, known limitations, and recent changes.
  3. **Interfaces**: Public APIs, CLI options, delimiters, data structures, and function signatures.
  4. **Failure Cases**: Error reporting, exception paths, invalid arguments, network/disk timeouts, and recovery strategies.
  5. **Testing**: Automated assertion-based test fixtures, expected output values, and test execution commands.
  6. **Compatibility**: Multi-platform parity (e.g. Windows PowerShell and POSIX Bash), backwards compatibility, and dialect rules.
  7. **Deployment**: Target file locations, binary placement, build cleanup, and environment configuration.
* **Autonomous Repository Exploration Invariant**: Whenever an answer can be determined from the codebase, the agent MUST inspect the repository itself (using `view_file`, `grep_search`, `list_dir`) BEFORE asking the user. Never ask questions whose answers are readily discoverable in the source code.
* **Selective High-Impact Inquiries Only**: The 7 dimensions serve as an analytical framework for internal codebase exploration, NOT as a mandatory questionnaire to mechanically recite to the user. Agents must NOT ask questions merely to be thorough; ask only on dimensions where an unresolved ambiguity directly changes the recommendation, design, or implementation.
* **Recommendation Transparency**: When proposing implementation options or plans, always explicitly label preferred paths as recommendations rather than absolute facts.
* **Zero-Assumption Discipline**: Agents must NEVER assume user intent, preferred architecture, or scope when ambiguity exists.
* **Pre-Modification Implementation Plan Gate**: Agents MUST NOT edit code files until:
  1. The user explicitly agrees on the design.
  2. The agent has presented a concise implementation plan (either via a structured `implementation_plan.md` artifact for architectural changes or an inline structured plan for focused tasks).

---

## 2. Headless & Non-Interactive Execution Protocols

### 2.1 Mandatory Headless Invocation
* **Non-Interactive Execution**: For all automated testing, verification suites, and headless script runs, agents must always supply explicit non-interactive flags (e.g., `--batch`, `-NonInteractive`, `--no-pause`, `-b`).
* **Interactive Blocking Shield**: Bare invocation of interactive REPLs or interactive script prompts without batch/non-interactive flags is strictly prohibited in automated sessions to eliminate stdin blocking and session hangs.

### 2.2 Execution Timeouts & Anti-Hang Guards
* **Mandatory Script Timeouts**: When executing unverified, newly written, or stress-test scripts, an engine or process execution timeout mechanism must be supplied (e.g., `--timeout=<ms>` or timeout wrapper).
* **Deterministic Abort**: If an infinite loop or deadlock occurs in the target script, the execution environment must abort deterministically with an error rather than hanging indefinitely.

---

## 3. Scoped Cleanup & Filesystem Invariants

### 3.1 Synchronous-Only Scoped Cleanup Invariant
* **Synchronous Invocation**: Build cleanup, intermediate object deletion, and test fixture teardown MUST ALWAYS run synchronously and finish BEFORE generating final walkthrough artifacts and delivering completion reports. Agents must NEVER background a cleanup command or yield a turn with a pending cleanup task.
* **Forbidden Whole-Repo Recursion**: Running unconstrained recursive file system scans across an entire repository (such as `Get-ChildItem -Path . -Recurse` or `find . -name ...` from repo root) is **STRICTLY FORBIDDEN**. Whole-repo recursion traverses `.git/`, stalls on loose object files, locks on open handles, and triggers task timeouts.
* **Scoped Targeting**: Cleanup must strictly target known intermediate directories (`build/`, `scratch/`, `test_run*`) using dedicated scoped utilities or scripts.

---

## 4. Engineering Quality & Implementation Discipline

### 4.1 Strict No-Stubs / No-Mocks Policy
* **Zero Partial Commits**: Never commit incomplete, mocked, or placeholder functions, statements, or handlers. Features must be implemented end-to-end with real operational paths across all relevant architectural layers.

### 4.2 Mandatory Expected-Results Assertion Testing
* **Assertion Verification**: Never conclude work by verifying that code merely executes without crashing. Automated test suites MUST assert actual runtime values/paths against exact expected outcomes.
* **Comprehensive Coverage**: Tests must cover typical usage, edge cases, boundary conditions, error handling, and clean resource cleanup.

### 4.3 Non-Destructive Rule Preservation
* **Surgical Rule Updates**: When updating project rules or agent guidelines, agents must NEVER overwrite, truncate, or wipe out existing domain-specific rules. Universal standards must be merged surgically into established rulebooks, preserving all project-specific invariants.

### 4.4 Multi-Layer Pre-Completion Audit Gate
* **Mandatory Turn Completion Audit**: Before concluding any task or generating a final walkthrough, the agent MUST run `sync_rules.ps1 -AuditOnly` against the active workspace to confirm that 100% of universal project and agent invariants are satisfied.
* **Zero Regression Obligation**: If an audit check fails or flags missing invariants, the agent must resolve the discrepancy immediately before delivering the final response.


---

## 5. Domain-Specific Agent Architectural Guidelines

> **Note**: Add project-specific agent constraints, build commands, and test workflows below.
