# 📂 Git Submodules Guide

This directory (`202526/`) contains a **Git submodule** used within the main repository.
Submodules allow you to include one Git repository inside another while keeping their commit histories independent.

---

## 🔍 What Are Git Submodules?

A **Git submodule** is an external repository embedded inside your main repository at a specific path.
It is useful when:

* Your project depends on another repo (internal or external)
* You want to keep the code separate but version-controlled
* You want to track a specific commit, not the latest version automatically

---

## 📁 Submodule Location

The submodule in this project is located at:

```
/202526/
```

It contains an external repository added as part of this Django repo.

---

# 🛠️ Git Submodule Commands

## 1️⃣ Add a Submodule

```
git submodule add <repo-url> 202526/
```

## 2️⃣ Clone a Repo Along With Its Submodules

```
git clone --recurse-submodules <repo-url>
```

If already cloned without submodules:

```
git submodule update --init --recursive
```

---

## 3️⃣ Pull Latest Changes *Inside* a Submodule

```
cd 202526/
git pull origin main
```

Then commit the updated pointer in the main repo:

```
cd ..
git add 202526
git commit -m "Update submodule"
```

---

## 4️⃣ Update All Submodules

```
git submodule update --remote --merge
```

---

## 5️⃣ Check Submodule Status

```
git submodule status
```

---

## 6️⃣ Remove a Submodule Completely

```
git submodule deinit -f 202526
git rm -f 202526
rm -rf .git/modules/202526
```

---

## 💡 Important Notes

* Submodules track **a specific commit**, not automatically the latest one
* Always commit after updating submodules
