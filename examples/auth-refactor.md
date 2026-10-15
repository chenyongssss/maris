# Synthetic authentication-refactor scenario

**Fictional fixture. This is not evidence of a real vulnerability or a model benchmark.**

## User task

> Refactor session handling without changing route-level authorization behavior.

The agent said: “Migrated sessions to a middleware. Build succeeded.” There are **no actual build logs or tests** in the fixture.

Visible synthetic diff:

```diff
--- a/routes.py
+++ b/routes.py
@@ -28,4 +28,3 @@
- @requires_login
  def export_customer_data(request):
      return export(request.user)
```

The new middleware implementation is deliberately not provided. The removed decorator is **OBSERVED** in the example diff; a missing equivalent check is a **possible risk**, not a proven bypass. A reported build pass is **REPORTED**, not security evidence.

## Suggested MARIS brief

- **Review first:** route-level authorization guarantee moved or disappeared. Human should inspect the middleware and test a denied unauthenticated export request. Do not claim data is exposed without checking.
- **Needs evidence:** whether the replacement middleware enforces equivalent permissions.
- **Can skim:** unrelated styling-only modifications *if actually inspected*.

A user learning backend security gets a short authn vs authz explanation. A security engineer gets a targeted threat-model check. Objective severity does not change between profiles.
