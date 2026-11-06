// Synchronous polling example; prefer the project's existing waiter.
// Return undefined while pending. All other values are successful results.
export interface WaitOptions {
  timeoutMs: number;
  intervalMs: number;
}

export async function waitFor<T>(
  probe: () => T | undefined,
  description: string,
  { timeoutMs, intervalMs }: WaitOptions
): Promise<T> {
  if (!Number.isFinite(timeoutMs) || timeoutMs <= 0 ||
      !Number.isFinite(intervalMs) || intervalMs <= 0) {
    throw new Error('timeoutMs and intervalMs must be finite positive numbers');
  }

  // A monotonic clock avoids changes to wall-clock time moving the deadline.
  const deadline = performance.now() + timeoutMs;
  while (true) {
    const remaining = deadline - performance.now();
    if (remaining <= 0) {
      throw new Error(`Timeout waiting for ${description} after ${timeoutMs}ms`);
    }

    const value = probe();
    if (value !== undefined) return value;

    await new Promise<void>(resolve =>
      setTimeout(resolve, Math.min(intervalMs, remaining))
    );
  }
}
