# ng-bootstrap <-> Angular <-> Bootstrap compatibility

Authoritative source: ng-bootstrap compatibility/dependencies table in the ng-bootstrap repo.
https://github.com/ng-bootstrap/ng-bootstrap
Rule: never guess versions. Verify against the official table when making changes.

Process:
1) Read Angular major from package.json: @angular/core
2) Pick matching @ng-bootstrap/ng-bootstrap major
3) Align bootstrap (CSS) version to the "tested with" line
4) Align @popperjs/core when using tooltip/popover/dropdown positioning

Recommended mapping (from ng-bootstrap "tested with" guidance):

| Angular major | ng-bootstrap major | Bootstrap CSS | Popper |
|---|---|---|---|
| 21 | 20.x | 5.3.8 | 2.11.8 |
| 20 | 19.x | 5.3.6 | 2.11.8 |
| 19 | 18.x | 5.3.3 | 2.11.8 |
| 18 | 17.x | 5.3.2 | 2.11.8 |
| 17 | 16.x | 5.3.2 | 2.11.8 |
| 16 | 15.x | 5.2.3 | 2.11.6 |
| 15 | 14.x | 5.2.3 | 2.11.6 |

Notes:
- "Tested with" is the safest default. Deviate only with intent and a repro.
- Bootstrap JS bundle is NOT part of this contract. In Angular, prefer ng-bootstrap for behavior.
- If the repo is Angular 20, use ng-bootstrap 19.x and Bootstrap 5.3.6.
