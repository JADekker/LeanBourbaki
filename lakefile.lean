import Lake
open Lake DSL

package «LeanBourbaki» where
  -- Settings applied to both builds and interactive editing
  leanOptions := #[
    ⟨`pp.unicode.fun, true⟩, -- pretty-prints `fun a ↦ b`
    ⟨`pp.proofs.withType, false⟩,
    ⟨`autoImplicit, false⟩,
    ⟨`relaxedAutoImplicit, false⟩
  ]
  -- add any additional package configuration options here

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"

@[default_target]
lean_lib LeanBourbaki where
  -- add any library configuration options here

/-- `lake exe checkYamlCustom` verifies that all declarations referred to in `LeanBourbaki/*.yaml`
files exist. -/
lean_exe checkYamlCustom where
  srcDir := "scripts"
  supportInterpreter := true
