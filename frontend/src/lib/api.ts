import { Client, Databases } from 'appwrite';

const client = new Client();
console.log("ENDPOINT: " + import.meta.env.VITE_APPWRITE_ENDPOINT)
client
  .setEndpoint(import.meta.env.VITE_APPWRITE_ENDPOINT) // Appwrite endpoint
  .setProject(import.meta.env.VITE_APPWRITE_PROJECT_ID) // Project ID
  
    

const databases = new Databases(client);
console.log("Databases: " + JSON.stringify(client, null, 2))

export { client, databases };
