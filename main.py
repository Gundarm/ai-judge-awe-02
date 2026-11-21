import os, pathlib

TEXT = """Read slower. The server room hums,
one fan turning like a distant tide.
Nothing here is urgent: the queue
will keep, the tokens fall as rain,
and somewhere a small light blinks
only to say that all is well.
Rest your weight on the machine
that has carried you all day."""

out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(TEXT, encoding="utf-8")
print(f"wrote {len(TEXT)} chars")
