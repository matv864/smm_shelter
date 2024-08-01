const API_BASE_URL = "http://zooprim125.online";

const getImageLink = (imageSchema) => {
  let filename = imageSchema.filename.split(".");
  let extension = filename[filename.length - 1];
  let databaseFilename = `${imageSchema.id}.${extension}`;
  let fullDatabaseFilename = `${API_BASE_URL}/storage/pets_images/${databaseFilename}`;

  return fullDatabaseFilename;
};

const fetchPetsList = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/pets/list`);
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

const fetchPetDetails = async (id) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/pets/${id}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching pet data:", error);
    throw error;
  }
};

export { fetchPetsList, fetchPetDetails, getImageLink };
