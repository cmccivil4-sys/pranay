export async function idbSet(key: string, value: string): Promise<void> {
  const openReq = indexedDB.open('aicm-cache', 1);
  openReq.onupgradeneeded = () => {
    openReq.result.createObjectStore('kv');
  };

  await new Promise<void>((resolve, reject) => {
    openReq.onsuccess = () => {
      const tx = openReq.result.transaction('kv', 'readwrite');
      tx.objectStore('kv').put(value, key);
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error);
    };
    openReq.onerror = () => reject(openReq.error);
  });
}
