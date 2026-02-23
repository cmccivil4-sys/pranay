'use client';

import { useState } from 'react';

export function CircuitScanner() {
  const [fileName, setFileName] = useState('');

  return (
    <section className="rounded-xl border border-amber-500/30 p-4">
      <h2 className="font-semibold">Handwritten Circuit Scanner</h2>
      <input type="file" className="mt-2" onChange={(e) => setFileName(e.target.files?.[0]?.name || '')} />
      <p className="mt-2 text-sm text-slate-300">Selected: {fileName || 'none'}</p>
    </section>
  );
}
