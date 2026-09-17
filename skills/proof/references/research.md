# proof research ledger

## Source 1

Title: Test sizes

Author / Organization: Google Testing Blog

Publication date: 2010-12-13

Version: Web article

URL: https://testing.googleblog.com/2010/12/test-sizes.html

Source type: official docs

What it establishes:
Tests trade scope, fidelity, speed, and isolation; larger is not automatically better.

What this skill adopts:
Choose the cheapest boundary that can faithfully fail for the target behavior or invariant.

What it does NOT establish:
It does not prescribe an arbitrary coverage percentage or require every bug to be reproduced at unit level.

Numbers taken from source:
No numerical coverage target is adopted.

Reverify when:
Project risk or stronger testing evidence changes.

## Test behavior and implementation detail

Title: Testing on the Toilet: Know Your Test Doubles

Author / Organization: Google Testing Blog

Publication date: 2018

Version: Web article

URL: https://testing.googleblog.com/2018/07/testing-on-toilet-know-your-test-doubles.html

Source type: official docs

What it establishes:
Test doubles differ in how they replace collaborators and can make tests depend
on details that are not the behavior under test.

What this skill adopts:
Use doubles at non-owned or impractical boundaries and prefer outcome assertions
over mock interaction choreography.

What it does NOT establish:
It does not ban all mocks or determine the right test boundary for a specific
repository.

Numbers taken from source:
None.

Reverify when:
The project test architecture or relevant testing guidance changes.

## Deterministic test design

Title: Testing on the Toilet: Avoid Sleep

Author / Organization: Google Testing Blog

Publication date: 2015

Version: Web article

URL: https://testing.googleblog.com/2015/04/testing-on-toilet-dont-sleep-on-it.html

Source type: official docs

What it establishes:
Timing sleeps make tests slower and less reliable than waiting for a specific
condition or using deterministic synchronization.

What this skill adopts:
Prefer condition-based waiting and controlled clocks/scheduling over arbitrary
sleep in asynchronous and concurrent tests.

What it does NOT establish:
It does not guarantee a test is race-free or prescribe a universal timeout.

Numbers taken from source:
No timeout value is adopted.

Reverify when:
The asynchronous runtime, synchronization primitive, or test runner changes.
