# Deploy-Freeze-Discipline - Human Guide

Implement freeze windows with exception tracking.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Runs high-stakes change freezes properly: clear windows, a legitimate exception path so nobody improvises, a rehearsed hotfix lane, and an official thaw.

## When to use it

Holiday seasons, major launches, audit periods. Triggers: code freeze, deploy freeze, change window.

## When NOT to use it

Small teams shipping low-risk changes may not need formal freezes. Don't freeze what you can't enforce.

## How you know it worked

Exception log exists and is short; hotfix lane proved itself if used; unfreeze happened on schedule.
