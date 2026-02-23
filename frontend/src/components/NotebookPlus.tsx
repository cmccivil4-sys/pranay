'use client';

import { useState } from 'react';
import { idbSet } from '../lib/idb';

export function NotebookPlus() {
  const [note, setNote] = useState('Ohm law links voltage, current, resistance.');

  const saveOffline = async () => {
    await idbSet('latest-note', note);
  };

  return (
    <section className="rounded-xl border border-cyan-500/30 p-4">
      <h2 className="font-semibold">Notebook++</h2>
      <textarea className="mt-2 w-full bg-slate-900 p-2" value={note} onChange={(e) => setNote(e.target.value)} />
      <button className="mt-2 px-3 py-1 bg-cyan-600 rounded" onClick={saveOffline}>Save Offline</button>
    </section>
  );
}
