import { Client, Databases } from 'appwrite';

const client = new Client();
client
  .setEndpoint(import.meta.env.VITE_APPWRITE_ENDPOINT) // Appwrite endpoint
  .setProject(import.meta.env.VITE_APPWRITE_PROJECT_ID); // Project ID

const databases = new Databases(client);

export { client, databases };
