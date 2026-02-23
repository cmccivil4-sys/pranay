'use client';

import { useState } from 'react';
import { apiPost } from '../lib/api';

export function NumericalSolver() {
  const [question, setQuestion] = useState('Given V=12V and R=4Ω find I and P');
  const [result, setResult] = useState<string>('');

  const solve = async () => {
    const data = await apiPost('/api/v1/solver/solve', { question, level: 'adaptive' });
    setResult((data.steps || []).join(' | '));
  };

  return (
    <section className="rounded-xl border border-emerald-500/30 p-4">
      <h2 className="font-semibold">AI Numerical Solver</h2>
      <input className="mt-2 w-full bg-slate-900 p-2" value={question} onChange={(e) => setQuestion(e.target.value)} />
      <button className="mt-2 px-3 py-1 bg-emerald-600 rounded" onClick={solve}>Solve</button>
      <p className="mt-2 text-sm">{result}</p>
    </section>
  );
}
