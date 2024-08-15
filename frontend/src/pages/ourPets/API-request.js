const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

if (!API_BASE_URL) {
  throw new Error("API_BASE_URL is not defined in environment variables.");
}

const getImageLink = (imageSchema) => {
  if (!imageSchema.filename || !imageSchema.id) {
    console.error("Invalid imageSchema:", imageSchema);
    return "img-for-help-animals.png";
  }

  let filename = imageSchema.filename.split(".");
  let extension = filename[filename.length - 1];
  let databaseFilename = `${imageSchema.id}.${extension}`;
  let fullDatabaseFilename = `${API_BASE_URL}/storage/pets_images/${databaseFilename}`;

  return fullDatabaseFilename;
};

const fetchPetsList = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/pets/list`);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();

    if (!Array.isArray(data)) {
      throw new Error("Fetched data is not an array");
    }

    const processedData = await Promise.all(
      data.map(async (post) => {
        if (post.images && post.images.length > 0) {
          const firstImageLink = getImageLink(post.images[0]);
          return { ...post, firstImageLink };
        }
        return { ...post, firstImageLink: "img-for-help-animals.png" };
      })
    );

    return processedData;
  } catch (error) {
    console.error("Error fetching posts:", error);
    throw error;
  }
};

export { fetchPetsList, getImageLink };
