const API = "http://localhost:8000";

export async function extractWebsite(
  url: string,
  prompt: string
) {
  const response = await fetch(`${API}/extract`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url,
      prompt,
    }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(error || "Extraction failed");
  }

  return response.json();
}

export async function downloadCSV(
  items: Record<string, any>[]
) {
  const response = await fetch(`${API}/extract/csv`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      items,
    }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(error || "CSV generation failed");
  }

  const blob = await response.blob();

  const downloadUrl = window.URL.createObjectURL(blob);

  const link = document.createElement("a");

  link.href = downloadUrl;
  link.download = "intelliscout_results.csv";

  document.body.appendChild(link);

  link.click();

  link.remove();

  window.URL.revokeObjectURL(downloadUrl);
}