# Two-Pen Zero-Knowledge Proof

The goal is simple:

> **Prove that you can distinguish two differently colored pens without revealing their colors.**

## The Idea

Imagine Alice has two pens, one red and one blue, and she wants to prove to Bob that she can distinguish between the two pens without telling him their colors.

## The Protocol

Bob holds the two pens, one in each hand. He can randomly choose to **switch the pens between his hands or leave them unchanged**.

Alice then tells Bob whether he switched the pens or not.

After repeating this many times, if Alice can consistently answer correctly, Bob gains confidence that Alice can distinguish between the two pens.

The key point is that Alice never tells Bob the colors of the pens.

## Why is this Zero-Knowledge?

Alice proves that she has the **knowledge needed to distinguish the two pens** without revealing the actual information she knows — the colors.

The verifier learns that Alice can distinguish the pens, but does not learn which pen is red or blue.
